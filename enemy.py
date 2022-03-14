import pygame
import random

COLORS = ["R", "G", "B"]

class Enemy:
    
    def __init__(self) -> None:
        
        # We set the enemy's starting position using a random x value
        self.position = (random.randint(50, 750), 50)
        
        # We give the enemy a random color ("R", "G" or "B")
        self.color = random.choice(COLORS)
        
        # We load the enemy's image using its color
        self.image = pygame.image.load("assets/enemy_" + self.color + ".png")
        
    # We return the enemy's position
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    # We modify the enemy's position
    def set_position(self, new_postion :tuple[int, int]) -> None:
        self.position = new_postion
    
    # We return the enemy's color
    def get_color(self) -> str:
        return self.color
    
    # We return the enemy's image
    def get_image(self) -> pygame.surface.Surface:
        return self.image
    
    # We move the enemy by one pixel towards the bottom of the screen
    def move_down(self) -> None:
        self.position = (self.position[0], self.position[1] + 1)