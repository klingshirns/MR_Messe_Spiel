"""
Messe Spiel - Main Class
"""

import arcade

from player import Player
from drawText import DrawText
import quiz

#-----------------------------------------------------------------
#Constans
#-----------------------------------------------------------------

#SCREEN_WIDTH = 1920
#SCREEN_HEIGHT = 1050

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#SCREEN_WIDTH = 1400
#SCREEN_HEIGHT = 1000


SCREEN_TITLE = "MR Messe Spiel"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE =128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.8
PLAYER_JUMP_SPEED = 14

# Player starting position
PLAYER_START_X = 64
PLAYER_START_Y = 1000

# Layer Names from our TileMap
LAYER_NAME_PLATFORMS = "ground"
LAYER_NAME_COINS = "coins"
LAYER_NAME_LEVEL_PORTAL = "level_portal"
LAYER_NAME_INFO_BOXES = "info_boxes"
LAYER_NAME_WIZZARD = "wizzard"

#-----------------------------------------------------------------


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

        #Level
        self.level = 0

        #Level entering Key (Enter)
        self.level_key = False

        # Holds map names
        self.maps = None

        # Hold the loaded info Box to give it to draw element
        self.load_info_box = None

        #Should load Info Box?
        self.should_load_info_box = False

        self.init_text()

        #setting the background-color for the map
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)




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

            LAYER_NAME_LEVEL_PORTAL: {
                "use_spatial_hash": True
            },

            LAYER_NAME_INFO_BOXES: {
                "use_spatial_hash": True
            },

            LAYER_NAME_WIZZARD: {
                "use spatial hash": True
            }
        }

        # Array to hold map names
        self.maps = ["welcome_area", "Fachkraft_für_lagerlogistik", "Industriekaufleute", 
                    "Fachinformatiker", "IT-Systemelektroniker", "Elektroniker", 
                     "Mechatroniker", "Industriemechaniker", "Werkzeugmechaniker", "Zerspannungsmechaniker"]

        current_map = self.maps[self.level] #get current map_name from Array with index
        map_name = f"../../assets/maps/{current_map}.tmx" # safe current map name with path

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options, hit_box_algorithm="Detailed")

        # Calculate the right edge of the map for viewport scrolling
        # /2 because tile scaling is 0.5
        self.map_width = ((self.tile_map.tiled_map.map_size.width) * self.tile_map.tiled_map.tile_size.width) / 2


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
        self.background = arcade.load_texture(f"../../assets/images/background/Teams_hintergrund_Digi_Netz-210915.jpg")

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
        arcade.draw_lrwh_rectangle_textured(0, -1000,
                                            7680, 4320,
                                            self.background)


        # Draw our Scene
        self.scene.draw()

        self.text_1.draw()
        self.text_2.draw()
        self.text_3.draw()
        self.text_4.draw()
        self.text_5.draw()
        self.text_6.draw()
        self.text_7.draw()
        self.text_8.draw()
        self.text_9.draw()


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

        # Consts to stop camera at the end
        
        stop_camera = self.map_width - SCREEN_WIDTH
        if screen_center_x > stop_camera:
            screen_center_x = stop_camera


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

        # If portal was hit, check if key was pressed and load next level if so
        if len(portal_hit) > 0:
            if self.level_key:
                self.level = int(portal_hit[0].properties["ID"])
                self.setup()

        # Is the player standing in front of a Info Box?
        # If yes, put it in a variable
        info_box_hit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_INFO_BOXES])

        # Takes the object which was hit
        for info_box in info_box_hit:
            if self.level_key: # Checks if the button to activate the info box was pressed
                
                info_box_id = int(info_box.properties["ID"]) #Get info Box id

                info_boxes = ["info_electro_it", "info_electro"] #Array for info_boxes (filename)
                info_box = info_boxes[info_box_id] # Get info box from array
                # loading info box image
                self.load_info_box = arcade.load_texture(f"../../assets/images/Info_Boxes/{info_box}.jpg")
                # sets value to draw info box to true
                self.should_load_info_box = True

        # Checks if the player colided with wizzardand puts it in a variable
        wizzard_hit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_WIZZARD])

        for wizzard in wizzard_hit:
            if self.level_key: 

                quiz.main()

                wizzard_id = int(wizzard.properties["ID"])

                self.level = wizzard_id
                self.level_key = False

                self.setup()

        # Position the camera
        self.center_camera_to_player()

        
        # Did the player fall off the map?
        if self.player_sprite.center_y < -100:

            #reset player to starting position
            self.player_sprite.center_x = PLAYER_START_X
            self.player_sprite.center_y = PLAYER_START_Y

        # Coordinates player can not move further 
        stop_player_right_edge = self.map_width - 32
        stop_player_left_edge = 32

        # Check if player got to one of the edges
        if self.player_sprite.center_x > stop_player_right_edge:
            self.player_sprite.center_x -= 16
        if self.player_sprite.center_x < stop_player_left_edge:
            self.player_sprite.center_x += 16

    def init_text(self):

        self.text_1 = None
        self.text_2 = None
        self.text_3 = None
        self.text_4 = None
        self.text_5 = None
        self.text_6 = None
        self.text_7 = None
        self.text_8 = None
        self.text_9 = None
        self.text_10= None

        if self.level == 0:
            self.drawWelcomeArea()

        elif self.level == 1:
            self.drawFachkraftLagerlogistik()

        elif self.level == 2:
            self.drawKaufmännisch()

        elif self.level == 3:
            self.drawFachinformatiker()

        elif self.level == 4:
            self.drawElectroIT()

        elif self.level == 5:
            self.drawElectro()

        elif self.level == 6:
            self.drawMechatronik()

        elif self.level == 7:
            self.drawIndustriemechanik()

        elif self.level == 8:
            self.drawWerkzeugmechanik()

        elif self.level == 9:
            self.drawZerspannung()

        else:
                #Default
                pass


    def drawWelcomeArea(self):


        # ID 1
        self.text_1 = arcade.Text(
            "Fachkraft - Lagerlogistik",
            1630,
            430,
            color= arcade.color.WHITE,
            font_size= 26,
            font_name=("Comic Sans MS")
        )

         
        # ID 2
        self.text_2 = arcade.Text(
            "Kaufmännisch",
            start_x= 2940,
            start_y= 880,
            color= arcade.color.WHITE,
            font_size= 26,
            font_name=("Comic Sans MS")
        )

        # ID 3
        self.text_3 = arcade.Text(
            "Fachinformatiker",
            start_x = 1680,
            start_y = 1400,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 4
        self.text_4 = arcade.Text(
            "Elektro - IT",
            start_x = 350,
            start_y = 1400,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 5
        self.text_5 =arcade.Text(
            "Elektro",
            start_x = 2980,
            start_y = 2300,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 6
        self.text_6 = arcade.Text(
            "Mechatronik",
            start_x = 4560,
            start_y = 2170,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 7
        self.text_7 = arcade.Text(
            "Industriemeachaniker",
            start_x = 6000,
            start_y = 2000,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 8
        self.text_8 = arcade.Text(
            "Werkzeugmechaniker",
            start_x = 6500,
            start_y = 2200,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 9
        self.text_9 = arcade.Text(
            "Zerspanner",
            start_x = 7000,
            start_y = 1200,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        self.count_text = 9

    def drawFachkraftLagerlogistik(self):
        pass

    def drawKaufmännisch(self):
        pass

    def drawFachinformatiker(self):
        pass

    def drawElectroIT(self):
        pass

    def drawElectro(self):
        pass

    def drawMechatronik(self):
        pass

    def drawIndustriemechanik(self):
        pass

    def drawWerkzeugmechanik(self):
        pass

    def drawZerspannung(self):
        pass
    
    
def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()