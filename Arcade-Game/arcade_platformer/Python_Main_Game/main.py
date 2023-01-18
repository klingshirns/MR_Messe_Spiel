"""
Messe Spiel - Main Class
"""

import arcade

from player import Player
from TextConstructor import TextObj
import quiz
import os

#-----------------------------------------------------------------
#Constans
#Landscape Fromat
#SCREEN_WIDTH = 1920
#SCREEN_HEIGHT = 1050
#or
#Development Format
#SCREEN_WIDTH = 1000
#SCREEN_HEIGHT = 600
#or
#Portrait Format
SCREEN_WIDTH = 1540
SCREEN_HEIGHT = 850

# Constants
#SCREEN_WIDTH = 1600
#SCREEN_HEIGHT = 1000
SCREEN_TITLE = "MR Messe Spiel"


# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
COIN_SCALING = 0.5
LIFE_SCALING = 0.3
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
LAYER_NAME_DONT_TOUCH = "enemies"

#-----------------------------------------------------------------


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the windowich
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)

        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # Our Score
        self.score = 0

        # Holds background image
        self.background_image = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our life in hearts
        self.heart = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        #Level
        self.level = 0

        # Life
        self.life = 3

        # Reset Life
        self.reset_life = True
        #Score 
        self.score = 0

        #Level entering Key (Enter)
        self.level_key = False

        # Holds map names
        self.maps = None

        # Hold the loaded info Box to give it to draw element
        self.load_info_box = None

        # Should Info box beeing loaded
        self.should_load_info_box = False

        #setting the background-color for the map
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # cache text objects for drawing
        self.text_1 = None
        self.text_2 = None
        self.text_3 = None
        self.text_4 = None
        self.text_5 = None
        self.text_6 = None
        self.text_7 = None
        self.text_8 = None
        self.text_9 = None

        # variable for text objects 
        self.to1 = None
        self.to2 = None
        self.to3 = None
        self.to4 = None
        self.to5 = None
        self.to6 = None
        self.to7 = None
        self.to8 = None
        self.to9 = None


    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # initiating texts, that are drawn on the screen 
        self.init_text()


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
            },

            LAYER_NAME_DONT_TOUCH: {
                "use spatial hash": True
            }
        }


        # Array to hold map names
        self.maps = ["welcome_area", "Fachkraft_für_lagerlogistik", "Industriekaufleute", 
                    "Fachinformatiker", "IT-Systemelektroniker", "Elektroniker", 
                     "Mechatroniker", "Industriemechaniker", "Werkzeugmechaniker", "Zerspannungsmechaniker"]

        #get current map_name from Array with index
        current_map = self.maps[self.level] 
        # safe current map name with path
        map_name = f"../../assets/maps/{current_map}.tmx" 

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options, hit_box_algorithm="Detailed")

        # Calculate the right edge of the map for viewport scrolling
        # /2 because tile scaling is 0.5
        self.map_width = ((self.tile_map.tiled_map.map_size.width) * self.tile_map.tiled_map.tile_size.width) / 2

        self.map_height = ((self.tile_map.tiled_map.map_size.height) * self.tile_map.tiled_map.tile_size.height) / 2


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
        
        #------------------------------------------------------
        # Draw my texts
        #------------------------------------------------------

        self.text_1.draw()
        self.text_2.draw()
        self.text_3.draw()
        self.text_4.draw()
        self.text_5.draw()
        self.text_6.draw()
        self.text_7.draw()
        self.text_8.draw()
        self.text_9.draw()
        
        #------------------------------------------------------


        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        #Draw our Score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            25,
            25,
            arcade.csscolor.WHITE,
            35,
            font_name= ("Comic Sans MS")
        )

        # Draw our Life on screen, srolling it with the viewport
        life_text = f"Life: {self.life} "
        arcade.draw_text(
            life_text,
            25,
            800,
            arcade.color.WHITE,
            35,
            font_name = ("Comic Sans MS"),
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

        elif key == arcade.key.F10:
            self.set_fullscreen(not self.fullscreen)
            
        
    
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
        
        stopCameraSide = self.map_width - SCREEN_WIDTH
        if screen_center_x > stopCameraSide:
            screen_center_x = stopCameraSide
        
        stopCameraTopBottom = self.map_height - SCREEN_HEIGHT
        if screen_center_y > stopCameraTopBottom:
            screen_center_y = stopCameraTopBottom

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
                portal_id = int(portal_hit[0].properties["ID"])

                if portal_id == 99:
                    arcade.close_window()
                else:
                    self.level = portal_id
                    self.setup()

        # Is the player standing in front of a Info Box?
        # If yes, put it in a variable
        info_box_hit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_INFO_BOXES])

        # Takes the object which was hit
        for info_box in info_box_hit:
            if self.level_key: # Checks if the button to activate the info box was pressed
                
                #Get info Box id
                info_box_id = int(info_box.properties["ID"]) 

                #Array for info_boxes (filename)
                info_boxes = ["Fachkraft_Lagerlogistik", "Industriekaufleute", 
                             "Fachinformatiker", "IT_Systemelektroniker", 
                             "Elektroniker_für_Betriebstechnik", "Mechatroniker", "Zerspanungsmechaniker"] 

                # Get info box from arrays
                info_box = info_boxes[info_box_id] 

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

        # Did the plyer touch something they should not?
        if arcade.check_for_collision_with_list(
            self.player_sprite, self.scene[LAYER_NAME_DONT_TOUCH]
        ):
            # Remove life
            self.life -= 1

            # checks if life is under 1
            if self.life <= 1:
                
                self.level = 0
                self.life = 3
                self.score = 0

                self.setup()

            else:
                self.player_sprite.center_x = PLAYER_START_X
                self.player_sprite.center_y = PLAYER_START_Y


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

        self.selectText()

        self.text_1 = arcade.Text(
        self.to1._text,
        self.to1._startx,
        self.to1._starty,
        self.to1._color,
        self.to1._font_size,
        font_name= self.to1._font_name
        )

        self.text_2 = arcade.Text(
        self.to2._text,
        self.to2._startx,
        self.to2._starty,
        self.to2._color,
        self.to2._font_size,
        font_name= self.to2._font_name
        )

        self.text_3 = arcade.Text(
        self.to3._text,
        self.to3._startx,
        self.to3._starty,
        self.to3._color,
        self.to3._font_size,
        font_name= self.to3._font_name
        )

        self.text_4 = arcade.Text(
        self.to4._text,
        self.to4._startx,
        self.to4._starty,
        self.to4._color,
        self.to4._font_size,
        font_name= self.to4._font_name
        )

        self.text_5 = arcade.Text(
        self.to5._text,
        self.to5._startx,
        self.to5._starty,
        self.to5._color,
        self.to5._font_size,
        font_name= self.to5._font_name
        )

        self.text_6 = arcade.Text(
        self.to6._text,
        self.to6._startx,
        self.to6._starty,
        self.to6._color,
        self.to6._font_size,
        font_name= self.to6._font_name
        )

        self.text_7 = arcade.Text(
        self.to7._text,
        self.to7._startx,
        self.to7._starty,
        self.to7._color,
        self.to7._font_size,
        font_name= self.to7._font_name
        )

        self.text_8 = arcade.Text(
        self.to8._text,
        self.to8._startx,
        self.to8._starty,
        self.to8._color,
        self.to8._font_size,
        font_name= self.to8._font_name
        )

        self.text_9 = arcade.Text(
        self.to9._text,
        self.to9._startx,
        self.to9._starty,
        self.to9._color,
        self.to9._font_size,
        font_name= self.to9._font_name
        )
        
    
    def selectText(self):

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

        self.to1 = TextObj("Fachkraft - Lagerlogistik", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj("Kaufmännisch", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj("Fachinformatiker - Systemintegration", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj("Elektro - IT", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj("Elektro", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj("Mechatronik", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj("Industriemechaniker", "Arial", 26, 5860, 1990, arcade.color.WHITE)
        self.to8 = TextObj("Werkzeugmechaniker", "Arial", 26, 6625, 2250, arcade.color.WHITE)
        self.to9 = TextObj("Zerspaner", "Arial", 26, 7420, 1270, arcade.color.WHITE)

    def drawFachkraftLagerlogistik(self):
        
        self.to1 = TextObj("Willkommen!", "Arial", 26, 500, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawKaufmännisch(self):

        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawFachinformatiker(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawElectroIT(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawElectro(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawMechatronik(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawIndustriemechanik(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawWerkzeugmechanik(self):

        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    def drawZerspannung(self):
        
        self.to1 = TextObj(" ", "Arial", 26, 1630, 430, arcade.color.WHITE)
        self.to2 = TextObj(" ", "Arial", 26, 2940, 880, arcade.color.WHITE)
        self.to3 = TextObj(" ", "Arial", 26, 1680, 1400, arcade.color.WHITE)
        self.to4 = TextObj(" ", "Arial", 26, 350, 1400, arcade.color.WHITE)
        self.to5 = TextObj(" ", "Arial", 26, 2980, 2300, arcade.color.WHITE)
        self.to6 = TextObj(" ", "Arial", 26, 4560, 2170, arcade.color.WHITE)
        self.to7 = TextObj(" ", "Arial", 26, 6000, 2000, arcade.color.WHITE)
        self.to8 = TextObj(" ", "Arial", 26, 6500, 2200, arcade.color.WHITE)
        self.to9 = TextObj(" ", "Arial", 26, 7000, 1200, arcade.color.WHITE)

    
    
def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()