"""
Messe Spiel
"""

from time import time
from tkinter import Place
from turtle import speed
from typing import Optional
import arcade
import time
import json
from select import select

from player import Player


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
PLAYER_START_Y = 500

# Layer Names from our TileMap
LAYER_NAME_PLATFORMS = "ground"
LAYER_NAME_COINS = "coins"
LAYER_NAME_GOALS = "goals"

# Creating variable 'player' that holds the class 'Player'
# -> function does not need to be called seperately because of __init__
player = Player()

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
        self.level = 1

        #Reset Level
        self.reset_level = True
        
        # Where is the right edge of the map?
        self.end_of_map = 0

        #setting the background-color for the map
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)


        # Name of map file to load
        #map_name = f"../assets/level_{self.level:02}.tmx"
        map_name = f"../assets/maps/test.tmx"
        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer

        # use spatial hashing for detection.

        layer_options = {

            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },

            LAYER_NAME_COINS: {
                "use_spatial_hash": True
            },

            LAYER_NAME_GOALS: {
                "use_spatial_hash": True
            },
        }

        # Read in the tiled map

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = Player()
        self.player_sprite.center_x = 128
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # Set the background color

        if self.tile_map.background_color:

            arcade.set_background_color(self.tile_map.background_color)



        # Create the 'physics engine'

        self.physics_engine = arcade.PhysicsEnginePlatformer(

            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["ground"]

        )


        # Calculate the right edge of the my_map in pixels
        #self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()


        # Draw our Scene
        self.scene.draw()


        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )


    def on_key_press(self, key, modifiers):
        #Called whenever a key is pressed.

        
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        
        
    
    def on_key_release(self, key, modifiers):
        #Called when the user releases a key.

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
    
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
            self.player_sprite, self.scene["coins"]
        )

        #Update all sprites
        self.player_sprite.update()

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Add one to the score
            self.score += 1


        # Position the camera
        self.center_camera_to_player()

        
        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:

            #reset player to starting position
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y
            self.life -= 1 #remove one life

            #checks if life is under r equal zero
            if self.life <= 0:
            
                self.level = 1
                self.life = 3
                self.score = 0

                self.setup()

        
        # See if the player got to the goal
        if arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_GOALS]
        ): 
            # Set next level
            self.level +=1

            # If the next level would be higher than 3, reset to level 1
            if self.level > 3:
                self.level = 1
                self.score = 0
                self.life = 3

                self.setup()

            # Load next level
            self.setup()
        

        """
        # Teleport player to xx coordinates
        if arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_PORTAL]
        ):
            self.player_sprite.center_x = 
            self.player_sprite.center_y = 
        """


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()