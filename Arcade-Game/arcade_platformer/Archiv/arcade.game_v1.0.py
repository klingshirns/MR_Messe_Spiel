import arcade
import pathlib

# Game constants
# Window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Arcade Platformer"

# Scaling Constants
MAP_SCALING = 1.0

# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 20

# Assets path
ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"


class Platformer(arcade.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These lists will hold different sets of sprites
        self.coins = None
        self.background = None
        self.walls = None
        self.goals = None

        # One sprite for the player, no more is needed
        self.player = None

        # We need a physics engine as well
        self.physics_engine = None

        # Someplace to keep score
        self.score = 0

        # Which level are we on?
        self.level = 1


    def setup(self) -> None:
        """Sets up the game for the current level"""

        # Get the current map based on the level
        map_name = f"platform_level_{self.level:01}.tmx"
        map_path = ASSETS_PATH / map_name

        # What are the names of the layers?
        wall_layer = "ground"
        coin_layer = "coins"
        goal_layer = "goal"
        background_layer = "background"

        # Load the current map
        game_map = arcade.tilemap.read_tmx(str(map_path))

        # Load the layers
        self.background = arcade.tilemap.process_layer(
            game_map, layer_name=background_layer, scaling=MAP_SCALING
        )
        self.goals = arcade.tilemap.process_layer(
            game_map, layer_name=goal_layer, scaling=MAP_SCALING
        )
        self.walls = arcade.tilemap.process_layer(
            game_map, layer_name=wall_layer, scaling=MAP_SCALING
        )
        self.coins = arcade.tilemap.process_layer(
            game_map, layer_name=coin_layer, scaling=MAP_SCALING
        )

        # Set the background color
        background_color = arcade.color.FRESH_AIR
        if game_map.background_color:
            background_color = game_map.background_color
        arcade.set_background_color(background_color)

        # Create the player sprite, if they're not already setup
        if not self.player:
            self.player = self.create_player_sprite()

        # Move the player sprite back to the beginning
        self.player.center_x = PLAYER_START_X
        self.player.center_y = PLAYER_START_Y
        self.player.change_x = 0
        self.player.change_y = 0

        # Load the physics engine for this map
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.player,
            platforms=self.walls,
            gravity_constant=GRAVITY,
        )

    def create_player_sprite(self) -> arcade.AnimatedWalkingSprite:
        """Creates the animated player sprite

        Returns:
            The properly setup player sprite
        """
        # Where are the player images stored?
        texture_path = ASSETS_PATH / "images" / "player"

        # Setup the appropriate textures
        standing_path = texture_path / "einfachmacher2.png"

        # Load them all now
        standing_right_textures = [arcade.load_texture(standing_path)]

        # Create the sprite
        player = arcade.AnimatedWalkingSprite()

        # Add the proper textures

        player.stand_right_textures = standing_right_textures

        # Set the player defaults
        player.center_x = PLAYER_START_X
        player.center_y = PLAYER_START_Y
        player.state = arcade.FACE_RIGHT

        # Set the initial texture
        player.texture = player.stand_right_textures[0]

        return player

    def on_key_press(self, key: int, modifiers: int) -> None:
        """Arguments:
        key -- Which key was pressed
        modifiers -- Which modifiers were down at the time
        """

        # Check for player left or right movement
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.player.change_x = -PLAYER_MOVE_SPEED
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player.change_x = PLAYER_MOVE_SPEED

        # Check if player can jump
        elif key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player.change_y = PLAYER_JUMP_SPEED
            

def on_key_release(self, key: int, modifiers: int) -> None:
    """Arguments:
    key -- The key which was released
    modifiers -- Which modifiers were down at the time
    """

    # Check for player left or right movement
    if key in [
        arcade.key.LEFT,
        arcade.key.A,
        arcade.key.RIGHT,
        arcade.key.D,
    ]:
        self.player.change_x = 0

    # Check if player can climb up or down
    elif key in [
        arcade.key.UP,
        arcade.key.I,
        arcade.key.DOWN,
        arcade.key.K,
    ]:
        if self.physics_engine.is_on_ladder():
            self.player.change_y = 0

    def on_update(self, delta_time: float) -> None:
        """Updates the position of all game objects

        Arguments:
        delta_time {float} -- How much time since the last call
        """

        # Update the player animation
        self.player.update_animation(delta_time)

        # Update player movement based on the physics engine
        self.physics_engine.update()

        # Restrict user movement so they can't walk off screen
        if self.player.left < 0:
            self.player.left = 0

        # Check if we've picked up a coin
        coins_hit = arcade.check_for_collision_with_list(
            sprite=self.player, sprite_list=self.coins
        )

        for coin in coins_hit:
            # Add the coin score to our score
            self.score += int(coin.properties["point_value"])

            # Remove the coin
            coin.remove_from_sprite_lists()

        # Now check if we're at the ending goal
        goals_hit = arcade.check_for_collision_with_list(
        sprite=self.player, sprite_list=self.goals
        )

        if goals_hit:

            # Set up the next level
            self.level += 1
            self.setup()

    def on_draw(self) -> None:
        arcade.start_render()

        # Draw all the sprites
        self.background.draw()
        self.walls.draw()
        self.coins.draw()
        self.goals.draw()
        self.player.draw()


if __name__ == "__main__":
    window = Platformer()
    window.setup()
    arcade.run()