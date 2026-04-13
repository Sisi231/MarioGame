import random
from Classes.Enemy import Enemy
from Classes.Mario import Mario
from Classes.Fly import Fly
from Classes.Crab import Crab
from Classes.Turtle import Turtle
from Classes.Coin import Coin
from Classes import Platform
from Classes import Constants
import pyxel


class Board:
    """ This is the class which stores the game board, the main game elements and some
    global variables.

    Attributes:
        Mario (Mario): Mario instance. it stores mario objects.
        enemies (Enemy) : list of type enemy that stores the enemies that are on the board
        coins (coin) : list of type coin that stores the coins that are on the board
        high_score (int) : the current highest score
        game_state (str) : can be one of the following :"start_screen","game", "game_over"
        level(int) : level of the game, changing the speed of the spawning of enemies
        num_turtles, num_crabs, num_flies (int) : counter to append enemies in specific amount

        width (int)(readonly): represents the width of the board
        height (int)(readonly): represents the height of the board


    Methods:
        update(self) : the pyxel update method of the board class object. This is the function that updates every frame
        __update_game_elements(self) : this function is invoked in the update function, and accordingly,
         updates the elements of the game
        __draw_stats(self): this method draws the stats of the game and is invoked in the draw_game
        enemy_hit(self, enemy): method that checks if mario is above the enemy in order to flip it
        enemy_stand_coll(self, enemy): method that checks if an enemy who isn't flipped overlaps with mario
        kick_enemy(self, enemy): method who checks if mario has kicked an enemy after flipping it.
        pick_coin(self, coin): this method checks the collision of Mario and the coins he picks.
        pow_button(self): when this method is invoked, the pow button makes all the enemies flip on their back
        check_all_collisions(self): a method who checks all the collision between the elements in the game
        __draw_start_screen(self): method that draws the start screen of the game
        __draw_game_over_screen(self): method that draws the game over screen of the game
        __blinking_color(color): this method is invoked for the draw of the screens
        draw(self) : the pyxel draw method. Invokes different draw function according to game state
        draw_game(self): a method which invokes the draw functions of all the classes when the game starts
        """

    def __init__(self):
        self.mario = Mario(self.width / 2 - 8, self.height - 40)
        self.enemies = []
        self.coins = []
        self.high_score = 0
        self.game_state = "start_screen"
        self.level = 1
        self.num_turtles, self.num_crabs, self.num_flies = 0, 0, 0
        self.total, self.enems = 15, 15
        self.pow_use = 4  # because when the game starts, it hits the pow button

    @property
    def width(self):
        return 253

    @property
    def height(self):
        return 226

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, value):
        if type(value) != int or value < 0:
            raise ValueError("The high score must be an integer above 0! ")
        else:
            self.__high_score = value

    @property
    def game_state(self):
        return self.__game_state

    @game_state.setter
    def game_state(self, value):
        if type(value) != str:
            raise TypeError("The game state can be only a string")
        elif value not in ["start_screen", "game", "game_over"]:
            raise ValueError(
                "The game state must be one of the following: 'start_screen', 'game', 'game_over'")
        else:
            self.__game_state = value

    def update(self):
        """ The main update method of the game, checks the status of the game and
        invokes specific update methods accordingly."""

        if self.game_state == "start_screen" and pyxel.btnp(pyxel.KEY_SPACE):
            self.game_state = "game"
            if self.high_score < self.mario.score:
                self.high_score = self.mario.score
            self.mario = Mario(self.width / 2, self.height - 40)
            self.coins = []

        elif self.game_state == "game_over" and pyxel.btnp(pyxel.KEY_R) and self.level <= 4:
            if self.high_score < self.mario.score:
                self.high_score = self.mario.score
            self.game_state = "start_screen"
            self.mario = Mario(self.width / 2, self.height - 40)
            self.level = 1
            Platform.platforms.append(Platform.pow_button)
            self.pow_use = 4
            self.enemies = []
            self.coins = []

        elif self.game_state == "game":

            self.__update_game_elements()
            self.__check_all_collisions()
            self.__spawn_enemies()

            if random.randint(0, 1500) == 5:
                self.coins.append(Coin(48, 26, 0))
            elif random.randint(0, 2000) == 7:
                self.coins.append(Coin(206, 26, 1))

            for enemy in self.enemies:
                enemy.flippy()
            if self.enems == 0 and len(self.enemies) == 0 and self.level < 4:
                self.pow_use = 4
                Platform.platforms.append(Platform.pow_button)
                self.level += 1
                self.enems = 15
                self.total = 15
                self.game_state = "start_screen"
            if self.level > 4:
                self.game_state = "game_over"

    def __spawn_enemies(self):
        """ This function is being called in the update method, and spans the enemies in a different
        speed depending on the game level.
        """
        list_possible_enemies = [Crab(48, 26, 0), Crab(206, 26, 1),
                                 Turtle(48, 26, 0), Turtle(206, 26, 1),
                                 Fly(48, 26, 0), Fly(206, 26, 1)]
        if self.level == 1:
            if random.randint(0, 300) == 10 and self.total > 0:
                self.enemies.append(list_possible_enemies[random.randint(0, 5)])
                self.total -= 1
        elif self.level == 2:
            if random.randint(0, 250) == 10 and self.total > 0:
                self.enemies.append(list_possible_enemies[random.randint(0, 5)])
                self.total -= 1
        elif self.level == 3:
            if random.randint(0, 200) == 10 and self.total > 0:
                self.enemies.append(list_possible_enemies[random.randint(0, 5)])
                self.total -= 1
        elif self.level == 4:
            if random.randint(0, 120) == 10 and self.total > 0:
                self.enemies.append(list_possible_enemies[random.randint(0, 5)])
                self.total -= 1

    def __update_game_elements(self):
        """ a method that goes over the elements of the game and updates them."""
        self.mario.update()

        for coin in self.coins:
            coin.update()

        for enemy in self.enemies:
            self.enemy_stand_coll(enemy)
            self.enemy_hit(enemy)
            if enemy.health <= 0:
                self.enems -= 1
                self.enemies.remove(enemy)
            else:
                enemy.update()

    def __draw_stats(self):
        """ Method that draws the stats of the game"""
        pyxel.text(34, 18, str(self.mario.score), 7)
        pyxel.text(114, 18, str(self.high_score), 7)
        pyxel.text(27, 202, str(self.level), 7)

    def enemy_hit(self, enemy):
        """ Method to check if Mario collides with an enemy"""
        if self.mario.is_jumping:
            if (
                    enemy.y < self.mario.y - Constants.PLATFORM_WIDTH <= enemy.y + enemy.height
                    and self.mario.x < enemy.x + enemy.width
                    and self.mario.x + self.mario.width > enemy.x
            ):
                return True

    def enemy_stand_coll(self, enemy):
        """ a method that checks is mario comes in contact with a non flipped enemy and reduces its life """
        if not enemy.is_flipped and (
                self.mario.y + self.mario.height == enemy.y + enemy.height
                and self.mario.x < enemy.x + enemy.width
                and self.mario.x + self.mario.width > enemy.x
        ):
            return True

    def kick_enemy(self, enemy):
        """ This method returns a boolean value if the enemy is flipped and Mario kicked it"""
        if enemy.is_flipped and (
                self.mario.y + self.mario.height == enemy.y + enemy.height
                and self.mario.x < enemy.x + enemy.width
                and self.mario.x + self.mario.width > enemy.x
        ):
            return True

    def pick_coin(self, coin):
        """ This method returns a boolean value if Mario overlaps with a coin"""
        if (self.mario.y + self.mario.height == coin.y + coin.height
                and self.mario.x < coin.x + coin.width
                and self.mario.x + self.mario.width > coin.x):
            return True

    @staticmethod
    def check_enemy_collision(enemy1, enemy2):
        """Method that checks if two enemies are colliding with each other and swaps their direction"""
        if (
                enemy1.y == enemy2.y and
                enemy1.x < enemy2.x + enemy2.width and
                enemy1.x + enemy1.width > enemy2.x
        ):
            enemy1.direction, enemy2.direction = enemy2.direction, enemy1.direction

    def __pow_button(self):
        """ a method to check if pow button is bumped, so that all the enemies will flip over"""
        for enemy in self.enemies:
            for plat in Platform.platforms:
                if enemy.check_coll_bottom(plat):
                    enemy.flip()

    def __check_all_collisions(self):
        """ This function checks all the collisions of the main game loop"""

        for i in range(len(self.enemies)):
            for j in range(i + 1, len(self.enemies)):
                enemy1 = self.enemies[i]
                enemy2 = self.enemies[j]
                self.check_enemy_collision(enemy1, enemy2)

        for enemy in self.enemies:
            # Checking collisions between mario and the enemies on the same platform
            if self.enemy_stand_coll(enemy):
                self.mario.lives -= 1
                self.mario.x = self.width / 2 - 8
                self.mario.y = self.height - 40
                if self.mario.lives <= 0 or self.enems < 1:
                    self.game_state = "game_over"

            if self.kick_enemy(enemy):
                enemy.health -= 1
                if enemy.health <= 0:
                    self.enems -= 1
                    self.mario.score += 800
                    self.enemies.remove(enemy)

        for enemy in self.enemies:
            # Checking collisions between mario and the enemies to flip them
            if self.enemy_hit(enemy) and type(enemy) is Crab:
                enemy.health -= 1
                if enemy.health == 1:
                    enemy.flip()
                    enemy.health = 2
            elif self.enemy_hit(enemy) and enemy.health == 1:
                enemy.flip()

        for coin in self.coins:
            if self.pick_coin(coin):
                self.mario.score += 1000
                self.coins.remove(coin)

        if self.mario.is_jumping and self.mario.check_coll_top(Platform.pow_button) and self.pow_use > 0:
            self.__pow_button()
            self.pow_use -= 1

    def __draw_start_screen(self):
        """Draws the start screen"""
        pyxel.cls(0)
        # pyxel.blt(self.width / 2 - 32, self.height / 2 - 15, 0, 136, 56, 64, 32, 0)
        pyxel.blt(0, 0, 2, 0, 0, 256, 223)
        if self.level == 1:
            text = "Press Space to start"
        else:
            text = "Press Space to start next level"
        pyxel.text(self.width / 2 - len(text) * 2, self.height / 2 - 25, text, self.__blinking_color(7))
        self.__draw_stats()

    def __draw_game_over_screen(self):
        """Draws the game over screen"""
        pyxel.cls(0)
        pyxel.blt(0, 0, 2, 0, 0, 256, 223)
        pyxel.text(self.width / 2 - 18, 100, "Game Over", self.__blinking_color(7))
        if self.level > 4:
            pyxel.text(self.width / 2 - 34, 150, "All levels passed", self.__blinking_color(7))
        else:
            pyxel.text(self.width / 2 - 36, 150, "Press R to restart", self.__blinking_color(7))
        self.__draw_stats()

    @staticmethod
    def __blinking_color(color):
        """Makes a color blink and is controlled by the frame count. Returns the color and black alternatively"""
        if pyxel.frame_count % 30 < 15:
            return color
        else:
            return 0

    def draw(self):
        """ This is the primary draw method which invokes the elements draw method depending on the game state."""
        if self.game_state == "start_screen":
            self.__draw_start_screen()
        elif self.game_state == "game":
            self.__draw_game()
        elif self.game_state == "game_over":
            self.__draw_game_over_screen()

    def __draw_game(self):
        """ This method draws the game"""

        self.mario.draw()
        self.__draw_stats()
        if self.pow_use > 0:
            pyxel.blt(120, 161, 1, 97, 225, 16, 14)
        else:
            if Platform.pow_button in Platform.platforms:
                Platform.platforms.remove(Platform.pow_button)
        for enemy in self.enemies:
            enemy.draw()
        for coin in self.coins:
            coin.draw()
        pyxel.text(self.width / 2 - 10, 26, "Level " + str(self.level), self.__blinking_color(7))
