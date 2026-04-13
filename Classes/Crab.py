from Classes.Enemy import Enemy
import pyxel
from Classes import Constants


class Crab(Enemy):
    """ The crab class inherits all the attributes and methods from the parent class enemy.
    The attribute health is different, since the crab needs to be hit more in order to die.
    """
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.health = 3

    @property
    def width(self):
        return 15

    @property
    def height(self):
        return 15

    def update(self):
        super().update()

    def draw(self):
        if not self.is_flipped and not self.angry:
            pyxel.blt(self.x, self.y, 0, 5, 74, self.width, self.height, 0)
        elif self.is_flipped:
            pyxel.blt(self.x, self.y, 0, 5, 122, self.width, self.height, 0)
        elif self.angry:
            pyxel.blt(self.x, self.y, 0, 28, 98, self.width, self.height)
