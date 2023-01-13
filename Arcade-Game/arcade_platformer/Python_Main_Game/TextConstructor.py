"""
Constructor for Text Objects
"""

from multipledispatch import dispatch
import arcade

class TextObj:

    _text = ""
    _font_name = ""
    _font_size = 0
    _startx = 0
    _starty = 0
    _color = arcade.color.BLACK


    def __init__(self, text, font_name, font_size, startx, starty, color):
        
        self._text = text
        self._font_name = font_name
        self._font_size = font_size
        self._startx = startx
        self._starty = starty
        self._color = color