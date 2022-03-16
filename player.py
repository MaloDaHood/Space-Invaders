import pygame

import constants

class Player:
    def __init__(self) -> None:
        
        # We set the player's starting position
        self.position = (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        
        # We load the player's image
        self.image = pygame.image.load("assets/player.png")
        
        # We set the number of lives the player has
        self.lives = constants.PLAYER_LIVES
        
    # We set the player's position on the middle of the mouse cursor
    def set_position_on_cursor(self) -> None:
        # We offset the position to make it centered
        self.position = (pygame.mouse.get_pos()[0] - (self.image.get_width() // 2), pygame.mouse.get_pos()[1] - (self.image.get_height() // 2))
    
    # We return the image's rectangle with the right coordinates
    def get_rect(self) -> pygame.rect.Rect:
        rect = self.image.get_rect()
        rect.x = self.position[0]
        rect.y = self.position[1]
        return rect
    
    # We return True if the player is alive
    def is_alive(self) -> bool:
        # We check if the player still has lives left
        if self.lives > 0:
            return True
        # Otherwise we return False
        return False