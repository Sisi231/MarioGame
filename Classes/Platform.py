import pyxel
from Classes.Constants import *


class Platform:
    """
        Class platform is used to create all the platform that appear in the game.

        Attributes:
            self.x (int): x coordinate of the enemy
            self.y (int): y coordinate of the enemy
            self.width (int): the width of the platform
            self.height (int): the height of the platform
        """
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int or (val < 0 or val > 253):
            raise TypeError("The x must be an integer between 0-250")
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int or (val < 0 or val > PYXEL_HEIGHT):
            raise TypeError("The x must be an integer between 0-256")
        else:
            self.__y = val

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int or (val > PYXEL_WIDTH):
            raise TypeError("The value must be an integer between 0-256!")
        else:
            self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int or val > PYXEL_HEIGHT:
            raise TypeError("Must be an integer between 0- 223!")
        else:
            self.__height = val


# create all the platforms
up_left = Platform(0, 64, 111, 9)
up_right = Platform(144, 64, 111, 9)
mid_left = Platform(0, 120, 31, 9)
mid_mid = Platform(64, 112, 127, 9)
mid_right = Platform(224, 120, 24, 9)
bott_left = Platform(0, 160, 95, 9)
bott_right = Platform(160, 160, 95, 9)
bottom = Platform(0, 208, 248, 9)
pow_button = Platform(120, 161, 16, 14)
# store the platforms in a list
platforms = [mid_left, mid_mid, mid_right, up_left, up_right, bott_left, bott_right, bottom, pow_button]
