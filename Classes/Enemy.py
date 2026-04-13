import random
import pyxel
from Classes import Platform
from Classes import Constants


class Enemy:
    """
    Class enemy is the parent class of all the enemies in the game given their common attributes and methods.

    Attributes:
        self.x (int): x coordinate of the enemy
        self.y (int): y coordinate of the enemy
        self.health(int): the number of lives of the enemy
        self.is_flipped (bool): a boolean variable to represent if the enemy is flipped or not
        self.flip_timer (int): timer for the flip of the enemy to get back up
        self.speed(int): the speed of the enemy
        self.direction(int): values of 0 or 1 which represent the direction of movement

    Methods:
        flip(self): a methods that sets the is_flipped variable to True when invoked
        flippy(self): a method to decrease the flip counter when the enemy is flipped
        fall(self): fall movement when the enemy steps out of a platform
        check_coll_bottom(self, platform): method to check if the bottom of the enemy overlap with a platform
        update(self): the pyxel update method of the enemy class which is being invoked in the board.
    """
    def __init__(self, x: float, y: float, direction: int):
        self.x = x
        self.y = y
        self.health = 1
        self.is_flipped = False
        self.flip_timer = 0
        self.speed = 40
        # movement direction : 0, right and 1, left
        self.direction = direction
        self.angry = False

    @property
    def height(self):
        return 15

    @property
    def width(self):
        return 15

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, val):
        if val != 1 and val != 0:
            raise ValueError("The direction must be 0 or 1!")
        else:
            self.__direction = val

    def flip(self):
        # When this function is invoked, the enemy is being flipped on his back
        self.is_flipped = True
        self.flip_timer = 100

    def flippy(self):
        if self.is_flipped and self.flip_timer > 0:
            self.flip_timer -= 1
            self.speed = 0
        if self.flip_timer == 0 and self.is_flipped:
            self.is_flipped = False
            self.speed = 60
            self.angry = True

    def fall(self):
        if self.y < Platform.bottom.y-self.height:
            self.y += Constants.GRAVITY
            for platform in Platform.platforms:
                if self.check_coll_bottom(platform):
                    self.y = platform.y - self.height
        else:
            self.y = Platform.bottom.y-self.height

    def check_coll_bottom(self, platform):
        # Check for collision with a platform to land on the platform
        return (
                self.x < platform.x + platform.width and
                self.x + self.width > platform.x and
                self.y + self.height >= platform.y > self.y
        )

    def update(self):
        """The enemies move right or left depending on from which side of the screen they come out
            If for some reason two enemies touch each other, they turn to the other way."""
        if self.direction == 1:  # Left
            self.x -= self.speed * Constants.DELTA_TIME
            if self.x < -self.width:
                self.x = pyxel.width

        else:  # Right
            self.x += self.speed * Constants.DELTA_TIME
            if self.x > pyxel.width:
                self.x = -self.width
        self.fall()






