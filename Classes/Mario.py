import pyxel
from Classes import Constants
from Classes import Platform
import math

# Create a method which checks if the pow button is pressed and flips all enemies accordingly
# Make a counter, if in the entire game its being touched 3 times - it disappears

# Check that if an enemy is flipped, and we jump below it, it will turn
# if enemy is flipped more than 3 seconds, the become bigger and faster


class Mario:
    """ Mario class represents the player in the game.

    Attributes
        x (float):X coordinate of the player
        y (float):Y coordinate of the player
        lives (int): the number of lives that Mario have
        score (int): the score of the player
        self.is_jumping(boolean): True or False value if Mario is jumping or not
        width (int)(readonly): Width of the player
        height (int)(readonly): Height of the player
        speed (int)(readonly): Speed of the player
        self.jump_count (int): counter that decreases for the jump motion
        self.is_falling(boolean): True or False depending on if Mario falls of a platform

    Methods:
        move(self, direction): method to define the movement of Mario
        jump(self): method created to preform the jumping motion of Mario
        check_coll_bottom(self, platform): method to check if mario is standing on a platform
        check_coll_top(self, platform): method to check if Mario collides with a platform from below it
        update(self): the pyxel update method of Mario class
        draw(self): the pyxel draw method which draws Mario
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.is_jumping = False
        self.jump_count = 10
        self.is_falling = False

    @property
    def width(self):
        return 16

    @property
    def height(self):
        return 20

    @property
    def speed(self):
        return 150

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int and type(val) != float:
            raise TypeError("The value of x must be float or int!")
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int and type(val) != float:
            raise TypeError("y value must be integer or float!")
        else:
            self.__y = val

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, val):
        if type(val) != int:
            raise ValueError("Type of lives must be int!")
        else:
            self.__lives = val

    def move(self, direction):
        if direction == "RIGHT":
            self.x += self.speed * Constants.DELTA_TIME
            if self.x > pyxel.width:
                self.x = -self.width
        elif direction == "LEFT":
            self.x -= self.speed * Constants.DELTA_TIME
            if self.x < -self.width:
                self.x = pyxel.width
        elif direction == "UP":
            self.y -= self.speed * Constants.DELTA_TIME

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 10

    def check_coll_bottom(self, platform):
        """Check if an object is on the platform"""
        return (
                self.x < platform.x + platform.width and
                self.x + self.width > platform.x and
                self.y + self.height >= platform.y > self.y
        )

    def check_coll_top(self, platform):
        """Checks if Mario hits the bottom of the platform"""
        return (
                self.x < platform.x + platform.width and
                self.x + self.width > platform.x and
                self.y < platform.y + platform.height and
                self.y + self.height > platform.y
        )

    def update(self):
        on_platform = False
        # Check collision with platforms from the top
        if not self.is_jumping:
            for platform in Platform.platforms:
                if self.check_coll_bottom(platform):
                    self.y = platform.y - self.height
                    on_platform = True

        # Check collision with platforms from the bottom when jumping
        if self.is_jumping:
            on_top_platform = False  # Flag to check if Mario hits a platform from the bottom
            for platform in Platform.platforms:
                if self.check_coll_top(platform):
                    on_top_platform = True
                    self.is_jumping = False
                    self.y = platform.y + platform.height

            # # If Mario is still jumping and hasn't hit a platform from the top, apply gravity
            if not on_top_platform:
                self.y += Constants.GRAVITY

        if not on_platform and not self.is_jumping:
            # If not on a platform and not jumping, apply gravity
            self.y += Constants.GRAVITY

        # Check if Mario is within the screen bounds
        if self.y > pyxel.height - self.height:
            self.y = pyxel.height - self.height

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.move("RIGHT")
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.move("LEFT")

        if pyxel.btn(pyxel.KEY_SPACE) and on_platform:
            self.jump()

        if self.is_jumping:
            if self.jump_count >= -10:
                neg = 1  # if neg = 1, Mario is moving downwards
                if self.jump_count < 0:
                    neg = -1  # if neg = -1, Mario is moving upwards
                    self.is_jumping = False
                self.y -= (self.jump_count ** 2) * 13 * Constants.DELTA_TIME * neg

                # Check if Mario has reached the top of the jump or collided with a platform from the top
                if neg == -1:
                    for platform in Platform.platforms:
                        if round(self.y) == platform.y + platform.height:
                            self.is_jumping = False
                            self.y = platform.y + platform.height
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 2, 0, 0, 256, 223)
        # depending on in which direction mario is moving, his image will change (default - looking to the left)
        if pyxel.btn(pyxel.KEY_RIGHT):
            pyxel.blt(self.x, self.y, 1, 16, 27, self.width, self.height, 0)
            if self.is_jumping:
                pyxel.blt(self.x, self.y, 1, 112, 24, self.width, self.height, 0)
        else:
            pyxel.blt(self.x, self.y, 1, 16, 59, self.width, self.height, 0)
            if self.is_jumping:
                pyxel.blt(self.x, self.y, 1, 160, 24, self.width, self.height, 0)
        # mario's heads show how many lives Mario has
        if self.lives == 3:
            pyxel.blt(64, 25, 1, 50, 225, 36, 9)
        elif self.lives == 2:
            pyxel.blt(64, 25, 1, 50, 225, 23, 9)
        elif self.lives == 1:
            pyxel.blt(64, 25, 1, 50, 225, 10, 9)
