import pygame
import random
import time

import constants

class Enemy:
    
    def __init__(self) -> None:
        
        # We set the enemy's starting position using a random x value and a negative y value to make it look like it comes from outside the window
        self.position = (random.randint(50, 750), -50)
        
        # We give the enemy a random color ("R", "G" or "B")
        self.color = random.choice(constants.COLORS)
        
        # We load the enemy's image using its color
        self.image = pygame.image.load("assets/enemy_" + self.color + ".png")
        
        self.is_alive = True
        
        # We create a clock to know when the enemy can shoot
        self.__start_time = time.time()
        
        # We set a random flying speed for the enemy
        self.__flying_speed = random.randint(1, 3)
        
        # We set a random shooting speed for the enemy
        self.__shooting_speed = random.choice([1, 1.5, 2])
    
    # We move the enemy by self.__flying_speed pixel(s) towards the bottom of the screen
    def move_down(self) -> None:
        self.position = (self.position[0], self.position[1] + self.__flying_speed)
        
    # We check if the enemy is still on the screen
    def is_on_screen(self) -> bool:
        # We check if it hasn't reached the bottom of the screen
        if self.position[1] < constants.WINDOW_HEIGHT + 10:
            return True
        # Otherwise we return False
        return False
    
    # We check if the enemy can shoot
    def can_shoot(self) -> bool:
        # We check if the last shot was more than a second ago
        if time.time() - self.__start_time > self.__shooting_speed:
            # We reset the clock
            self.__start_time = time.time()
            return True
        # Otherwise we return False
        return False
    
    # We return the image's rectangle with the right coordinates
    def get_rect(self) -> pygame.rect.Rect:
        rect = self.image.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect