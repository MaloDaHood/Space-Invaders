from msilib.schema import Directory
from operator import truediv
import pygame

from player import Player
from enemy import Enemy

class Laser:
    
    def __init__(self, object :Player|Enemy) -> None:
        
        if isinstance(object, Player):
            
            self.position = (object.get_position()[0], object.get_position()[1] - (object.get_image().get_height() // 2))
        
            self.image = pygame.image.load("assets/laser_player.png")
            
            self.direction = -6
        
        else:
            
            self.position = (object.get_position()[0] - (object.get_image().get_width() // 2), object.get_position()[1] + (object.get_image().get_height() // 2))
        
            self.image = pygame.image.load("assets/laser_" + object.get_color() + ".png")
        
            self.direction = 6
            
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    def get_image(self) -> pygame.surface.Surface:
        return self.image
            
    def move(self) -> None:
        self.position = (self.position[0], self.position[1] + self.direction)
        
    def is_on_screen(self) -> bool:
        
        if self.position[1] < 800 and self.position[1] > -50:
            
            return True
        
        return False