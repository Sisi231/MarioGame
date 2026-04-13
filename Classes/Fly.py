from Classes.Enemy import Enemy
import random
from Classes import Constants
import pyxel
from Classes import Platform


class Fly(Enemy):

    """ This class represent the enemy fly. It inherits some attributes from the Enemy class.
    The health attribute represent the number of kicks it takes to kill it.
    The Fly inherits all the attributes from the enemy class, beside the update method which is a bit different.
    The basis is the same, but a few adjustments made for the movement of the fly (jumping motion).

    Attributes:
        we have added attributes for self.bounce and self.bounce_counter for the jumping motion.
    """

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.health = 1
        self.bounce = False
        self.bounce_counter = 7

    @property
    def width(self):
        return 15

    @property
    def height(self):
        return 15

    def update(self):
        super().update()
        # Doing the bounce movement of the fly, the counter will bounce the fly every 5 frames
        for platform in Platform.platforms:
            if self.check_coll_bottom(platform):
                if self.bounce_counter == 7:
                    if not self.bounce:
                        self.y -= self.speed * Constants.DELTA_TIME * 20
                        self.bounce = True
                    else:
                        self.fall()
                        self.bounce = False
                    self.bounce_counter = 0
                else:
                    self.bounce_counter += 1

    def draw(self):
        if not self.is_flipped and not self.angry:
            pyxel.blt(self.x, self.y, 0, 29, 154, self.width, self.height, 0)
        elif self.is_flipped:
            pyxel.blt(self.x, self.y, 0, 5, 179, self.width, self.height, 0)
        elif self.angry:
            pyxel.blt(self.x, self.y, 0, 5, 154, self.width, self.height)
