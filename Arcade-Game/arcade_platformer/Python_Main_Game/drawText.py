"""
Draw-Text
"""

import arcade

class DrawText:

    def __init__(self, map_id):

        
        if map_id == 0:

            self.drawWelcomeArea()

        elif map_id == 1:

            self.drawElectroIT()
        else:
            #Default
            pass
        

    def drawWelcomeArea(self):

        # ID 1
        arcade.draw_text(
            "Elektro-IT",
            1750,
            430,
            color= arcade.color.BLACK,
            font_size= 26,
            font_name=("Comic Sans MS")
        )
        
        # ID 2
        arcade.draw_text(
            "Elektro",
            start_x= 2980,
            start_y= 880,
            color= arcade.color.BLACK,
            font_size= 26,
            font_name=("Comic Sans MS")
        )

        # ID 3
        arcade.draw_text(
            "Fachinformatiker",
            start_x = 1680,
            start_y = 1400,
            color= arcade.color.BLACK,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 4
        arcade.draw_text(
            "Elektro - IT",
            start_x = 360,
            start_y = 1400,
            color= arcade.color.BLACK,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )


    
    # def drawElectroIT(self):

    #     arcade.draw_text(
    #         "Welcome to IT",
    #         start_x = 200,
    #         start_y= 180,
    #         color = arcade.color.WHITE,
    #         font_size= 26,
    #         font_name=("Comic Sans MS")
    #     )


