from Classes.Enemy import Enemy
from Classes import Constants
import pyxel


class Turtle(Enemy):

    """ Class turtle represents the enemy turtle. It inherits from the parent class enemy.
    The attribute health is set to 1, because this is the one kick it takes to kill it.
    """

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.health = 1

    @property
    def width(self):
        return 15

    @property
    def height(self):
        return 15

    def update(self):
        super().update()

    def draw(self):
        # Draw movement based on the exit direction, 1- left, 0-right
        if self.direction == 1:
            if not self.is_flipped and not self.angry:
                pyxel.blt(self.x, self.y, 0, 5, 18, self.width, self.height, 0)
            elif self.is_flipped:
                pyxel.blt(self.x, self.y, 0, 5, 42, self.width, self.height, 0)
            elif self.angry:
                pyxel.blt(self.x, self.y, 0, 124, 18, self.width, self.height)
        else:
            if not self.is_flipped and not self.angry:
                pyxel.blt(self.x, self.y, 0, 101, 18, self.width, self.height, 0)
            elif self.is_flipped:
                pyxel.blt(self.x, self.y, 0, 5, 42, self.width, self.height, 0)
            elif self.angry:
                pyxel.blt(self.x, self.y, 0, 144, 17, self.width, self.height)