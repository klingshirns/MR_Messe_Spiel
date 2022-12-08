"""
Draw - Class
"""

import arcade 

# CONSTANTS

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 200

class Draw():
    
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        
        

        # start_x and start_y make the start point for the text. We draw a dot to make it
        # easy too see the text in relation to its start x and y.
        start_x = 10
        start_y = SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 3
        self.fonts = arcade.Text(
            "Fonts:",
            start_x,
            start_y,
            arcade.color.FRENCH_WINE,
            DEFAULT_FONT_SIZE, bold=True,
        )

        # Move the y value down to create another line of text
        start_y -= DEFAULT_LINE_HEIGHT
        self.font_default = arcade.Text(
            "Default Font (Arial)",
            start_x,
            start_y,
            arcade.color.BLACK,
            DEFAULT_FONT_SIZE    
        )
