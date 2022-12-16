"""
Messe Spiel - Main Class
"""

import arcade

from player import Player
from drawText import DrawText


# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "MR Messe Spiel"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
COIN_SCALING = 0.5
GOAL_SCALING = 1
LIFE_SCALING = 0.3
SPRITE_PIXEL_SIZE =128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.8
PLAYER_JUMP_SPEED = 11

# Player starting position
PLAYER_START_X = 64
PLAYER_START_Y = 1000

# Layer Names from our TileMap
LAYER_NAME_PLATFORMS = "ground"
LAYER_NAME_COINS = "coins"
LAYER_NAME_GOALS = "goals"
LAYER_NAME_LEVEL_PORTAL = "level_portal"
LAYER_NAME_INFO_BOXES = "info_boxes"

# Creating variable 'player' that holds the class 'Player'
# -> function does not need to be called seperately because of __init__


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Holds background image
        self.background_image = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        # Keep track of the score
        self.score = 0

        # Do we need to reset the score
        self.reset_score = True

        #Level
        self.level = 0

        #Reset Level
        self.reset_level = True

        #Level entering Key (Enter)
        self.level_key = False

        # Holds map names
        self.maps = None

        # Hold the loaded info Box to give it to draw element
        self.load_info_box = None

        #Should load Info Box?
        self.should_load_info_box = False

        #setting the background-color for the map
        arcade.set_background_color(arcade.csscolor.GREY)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)


        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.

        layer_options = {

            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True
            },

            LAYER_NAME_COINS: {
                "use_spatial_hash": True
            },

            LAYER_NAME_GOALS: {
                "use_spatial_hash": True
            },

            LAYER_NAME_LEVEL_PORTAL: {
                "use_spatial_hash": True
            },

            LAYER_NAME_INFO_BOXES: {
                "use_spatial_hash": True
            },
        }

        # Array to hold map names
        self.maps = ["welcome_area", "electronic_it"]

        current_map = self.maps[self.level] #get current map_name from Array with index
        map_name = f"../../assets/maps/{current_map}.tmx" # safe current map name with path

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options, hit_box_algorithm="Detailed")


        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = Player()
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite("Player", self.player_sprite)

        
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # load background image
        self.background = arcade.load_texture(f"../../assets/images/background/background.gif")

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(

            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene[LAYER_NAME_PLATFORMS]
        )


    def on_draw(self):
        
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw background image
        arcade.draw_lrwh_rectangle_textured(0, 128,
                                            3000, 1000,
                                            self.background)


        # Draw our Scene
        self.scene.draw()

        DrawText(self.level)

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()


        arcade.draw_text(
            self.level,
            0,
            0,
            color = arcade.color.BLACK,
            font_size = 30,
        )

        # Checks bool value "should_load_info_box" and draws the image
        if self.should_load_info_box:
            arcade.draw_lrwh_rectangle_textured(0,0,SCREEN_WIDTH, SCREEN_HEIGHT, self.load_info_box)


    def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed.

        
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.ENTER:
            self.level_key = True

        # Set bool value for loading info box to false when pressing Escape
        elif key == arcade.key.ESCAPE: 
            self.should_load_info_box = False
        
    
    def on_key_release(self, key, modifiers):
        #Called when the user releases a key.

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
        
        elif key == arcade.key.ENTER:
            self.level_key = False
    
    #centering the camera to the player
    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_COINS]
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Add one to the score
            self.score += 1

        #Update all sprites
        self.player_sprite.update()

        
        # Checks if the player colided with a Level portal and puts it in a variable
        portal_hit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_LEVEL_PORTAL])

        # Takes the value from the level portal hit and changes Level Value + reloads game
        for level_portal in portal_hit:
            if self.level_key:

                self.level = int(level_portal.properties["ID"])

                self.setup() # Reloads Game
        
        # Is the player standing in front of a Info Box?
        # If yes, put it in a variable
        info_box_hit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_INFO_BOXES])

        # Takes the object which was hit
        for info_box in info_box_hit:
            if self.level_key: # Checks if the button to activate the info box was pressed
                
                info_box_id = int(info_box.properties["ID"]) #Get info Box id

                info_boxes = ["info_electro_it"] #Array for info_boxes (filename)
                info_box = info_boxes[info_box_id] # Get info box from array
                # loading info box image
                self.load_info_box = arcade.load_texture(f"../../assets/images/Info_Boxes/{info_box}.jpg")
                # sets value to draw info box to true
                self.should_load_info_box = True

        # Draw texts on screen
        DrawText(self.level)

        # Position the camera
        self.center_camera_to_player()

        
        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:

            #reset player to starting position
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()