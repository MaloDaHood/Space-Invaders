import pygame

import constants
from player import Player
from enemy import Enemy

class Laser:
    
    def __init__(self, object :Player|Enemy) -> None:
        
        # We check if the laser comes from the player
        if isinstance(object, Player):
            
            # We load the yellow laser's image in
            self.image = pygame.image.load("assets/laser_player.png")

            # We set its position to the center of the player's image 
            self.position = (object.position[0] + ((object.image.get_width() // 2) - (self.image.get_width() // 2)), object.position[1] - (object.image.get_height() // 2))
            
            # We set its direction (+/-) and speed (int)
            self.__direction = -constants.LASER_SPEED
        
        # Otherwise it comes from an enemy
        else:
            
            # We load the image of the laser depending of the color of the enemy that shot it
            self.image = pygame.image.load("assets/laser_" + object.color + ".png")

            # We set its position to the center of the enemy's image 
            self.position = (object.position[0] + ((object.image.get_width() // 2) - (self.image.get_width() // 2)), object.position[1] + (object.image.get_height() // 2) + 20)

            # We set its direction (+/-) and speed (int)
            self.__direction = constants.LASER_SPEED
            
        self.is_alive = True
            
    # We change the laser's position according to its direction and speed
    def move(self) -> None:
        self.position = (self.position[0], self.position[1] + self.__direction)
        
    # We check if the laser is still on the screen
    def is_on_screen(self) -> bool:
        # We check if it hasn't reached the bottom or top of the screen
        if self.position[1] < constants.WINDOW_HEIGHT and self.position[1] > -50:
            return True
        # Otherwise we return False
        return False
    
    # We return the image's rectangle with the right coordinates
    def get_rect(self) -> pygame.rect.Rect:
        rect = self.image.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect