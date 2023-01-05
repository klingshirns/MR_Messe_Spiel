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
            "Fachkraft - Lagerlogistik",
            1630,
            430,
            color= arcade.color.WHITE,
            font_size= 26,
            font_name=("Comic Sans MS")
        )
        
        # ID 2
        arcade.draw_text(
            "Kaufmännisch",
            start_x= 2940,
            start_y= 880,
            color= arcade.color.WHITE,
            font_size= 26,
            font_name=("Comic Sans MS")
        )

        # ID 3
        arcade.draw_text(
            "Fachinformatiker",
            start_x = 1680,
            start_y = 1400,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 4
        arcade.draw_text(
            "Elektro - IT",
            start_x = 350,
            start_y = 1400,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 5
        arcade.draw_text(
            "Elektro",
            start_x = 2980,
            start_y = 2300,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 6
        arcade.draw_text(
            "Mechatronik",
            start_x = 4560,
            start_y = 2170,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 7
        arcade.draw_text(
            "Industriemeachaniker",
            start_x = 6000,
            start_y = 2000,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 8
        arcade.draw_text(
            "Werkzeugmechaniker",
            start_x = 6500,
            start_y = 2200,
            color= arcade.color.WHITE,
            font_size= 22,
            font_name = ("Comic Sans MS")
        )

        # ID 9
        arcade.draw_text(
            "Zerspanner",
            start_x = 7000,
            start_y = 1200,
            color= arcade.color.WHITE,
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


