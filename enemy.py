import pygame
import random
import time

COLORS = ["R", "G", "B"]

class Enemy:
    
    def __init__(self) -> None:
        
        # We set the enemy's starting position using a random x value
        self.position = (random.randint(50, 750), 50)
        
        # We give the enemy a random color ("R", "G" or "B")
        self.color = random.choice(COLORS)
        
        # We load the enemy's image using its color
        self.image = pygame.image.load("assets/enemy_" + self.color + ".png")
        
        self.isAlive = True
        
        # We create a clock to know when the enemy can shoot
        self.start_time = time.time()
        
        # We set a random speed for the enemy
        self.speed = random.randint(1, 3)
        
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
    
    # We move the enemy by self.speed pixel(s) towards the bottom of the screen
    def move_down(self) -> None:
        self.position = (self.position[0], self.position[1] + self.speed)
        
    # We return True if the enemy is alive
    def is_alive(self) -> bool:
        return self.isAlive
    
    # We kill the enemy
    def die(self) -> None:
        self.isAlive = False
    
    # We check if the enemy is still on the screen
    def is_on_screen(self) -> bool:
        # We check if it hasn't reached the bottom of the screen
        if self.position[1] < 810:
            return True
        # Otherwise we return False
        return False
    
    # We check if the enemy can shoot
    def can_shoot(self) -> bool:
        # We check if the last shot was more than a second ago
        if time.time() - self.start_time > 1:
            # We reset the clock
            self.start_time = time.time()
            return True
        # Otherwise we return False
        return False
    
    # We return the image's rectangle with the right coordinates
    def get_rect(self) -> pygame.rect.Rect:
        rect = self.image.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect