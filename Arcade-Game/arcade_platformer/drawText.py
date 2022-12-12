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
            990,
            330,
            color= arcade.color.BLACK,
            font_size= 26,
        )
        
        # Mechatronics
        arcade.draw_text(
            "Mechatronik",
            start_x= 1480,
            start_y= 385,
            color= arcade.color.BLACK,
            font_size= 26,
        )
    
    def drawElectroIT(self):

        arcade.draw_text(
            "Welcome to IT",
            start_x = 200,
            start_y= 180,
            color = arcade.color.WHITE,
            font_size= 26,
        )


