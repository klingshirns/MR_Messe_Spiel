"""
Player-Class
"""

import arcade
import json

#CONSTANTS

# Index of textures (left or right)
TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1

# Charakter Scaling
CHARACTER_SCALING = 0.8

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = CHARACTER_SCALING
        self.textures = []

        player_path = self.load_player_path()

        texture = arcade.load_texture(player_path, hit_box_algorithm="Simple")
        self.textures.append (texture)
        texture = arcade.load_texture(player_path, flipped_horizontally=True)

        self.textures.append (texture)

        #Default
        self.texture = texture

    def update(self):
        
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Face Left or right
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures [TEXTURE_RIGHT]
    
    def load_player_path(self):

        #open the .json file, which contains the paths of the players
        file = open('json/player.json')

        #load the .json file
        player_file = json.load (file)

        #close the .json file
        file.close

        #create variable for the "players" container
        player_container = player_file['players']

        #create variable for the selected player
        selected_player = player_file['selectedPlayer']

        #checks which charackter is selected by a number [0;1;2;3]
        if player_file["selectedPlayer"] == selected_player:
            #loading the image path of the .json file and creating a variable for it
            player_path = (player_container[selected_player]["Imgpath"])

        return player_path