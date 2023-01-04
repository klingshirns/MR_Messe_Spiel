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

        # Elektro-IT
        arcade.draw_text(
            "Elektro-IT",
            1750,
            430,
            color= arcade.color.BLACK,
            font_size= 26,
            font_name=("Comic Sans MS")
        )
        
        # Mechatronics
        # arcade.draw_text(
        #     "Mechatronik",
        #     start_x= 1480,
        #     start_y= 385,
        #     color= arcade.color.BLACK,
        #     font_size= 26,
        #     font_name=("Comic Sans MS")
        # )

        # #Wizzard
        # arcade.draw_text(
        #     "Stelle mir ein paar Fragen!",
        #     start_x = 2330,
        #     start_y = 330,
        #     color= arcade.color.BLACK,
        #     font_size= 22,
        #     font_name = ("Comic Sans MS")
        # )
    
    # def drawElectroIT(self):

    #     arcade.draw_text(
    #         "Welcome to IT",
    #         start_x = 200,
    #         start_y= 180,
    #         color = arcade.color.WHITE,
    #         font_size= 26,
    #         font_name=("Comic Sans MS")
    #     )


