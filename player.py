import pygame

class Player:
    def __init__(self) -> None:
        
        # We set the player's starting position
        self.position = (350, 700)
        
        # We load the player's image
        self.image = pygame.image.load("assets/player.png")
        
    # We return the player's position
    def get_position(self) -> tuple[int, int]:
        return self.position
    
    # We set the player's position on the middle of the mouse cursor
    def set_position_on_cursor(self) -> None:
        # We offset the position to make it centered
        self.position = (pygame.mouse.get_pos()[0] - (self.image.get_width() // 2), pygame.mouse.get_pos()[1] - (self.image.get_height() // 2))
    
    # We return the player's image
    def get_image(self) -> pygame.surface.Surface:
        return self.image