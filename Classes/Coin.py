from Classes import Constants
from Classes import Platform
from Classes.Enemy import Enemy
import pyxel


class Coin(Enemy):
    """ a class which represents the coins that moves on the screen, inherits from class Enemy"""

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)

    @property
    def height(self):
        return 10

    @property
    def width(self):
        return 10

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 175, 176, self.width, self.height)

