import pygame

import constants

class Menu:
    
    def __init__(self) -> None:
        
        # We create the window 
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)
        # We give the window a name
        pygame.display.set_caption("Space Invaders")
        
        # We load the background image
        self.__backgroud = pygame.image.load("assets/background.png")
        # We scale the background to fit the window
        self.__backgroud = pygame.transform.scale(self.__backgroud, constants.WINDOW_SIZE)
        
        self.__running = True
        
        self.__cursor = pygame.Rect(pygame.mouse.get_pos(), (10, 10))
        
        self.__play_button = pygame.Rect((constants.WINDOW_WIDTH // 4, constants.WINDOW_HEIGHT // 4), (constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 8))
        
        self.__quit_button = pygame.Rect((constants.WINDOW_WIDTH // 4, constants.WINDOW_HEIGHT - (constants.WINDOW_HEIGHT // 2)), (constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 8))
        
        # We load the font
        self.__font = pygame.font.Font("assets/akira.otf", 60)
        
    def display(self) -> None:
        
        while self.__running:
            
            self.handle_inputs()
            
            self.window.blit(self.__backgroud, (0, 0))
            
            self.__cursor.topleft = pygame.mouse.get_pos()
            
            pygame.draw.rect(self.window, (255, 0, 0), self.__cursor)
            
            pygame.draw.rect(self.window, (255, 0, 0), self.__play_button, 2)
            
            pygame.draw.rect(self.window, (255, 0, 0), self.__quit_button, 2)
            
            self.display_text()
            
            pygame.display.flip()
            
            
    # We handle every input given by the player
    def handle_inputs(self) -> None:
        
        # We check each event that happened
        for event in pygame.event.get():
            
            # We check if the player pressed the close buton
            if event.type == pygame.QUIT:
                
                # We stop the game
                pygame.quit()
            
            # We check if the player pressed the mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pass
            
    def display_text(self) -> None:
        
        text = self.__font.render("PLAY", True, (255, 0, 0))
        
        self.window.blit(text, (self.__play_button.x + ((constants.WINDOW_WIDTH // 4) - (text.get_width() // 2)) , self.__play_button.y + ((constants.WINDOW_HEIGHT // 8) - (text.get_height() * 1.5))))

        text = self.__font.render("QUIT", True, (255, 0, 0))
        
        self.window.blit(text, (self.__quit_button.x + ((constants.WINDOW_WIDTH // 4) - (text.get_width() // 2)) , self.__quit_button.y + ((constants.WINDOW_HEIGHT // 8) - (text.get_height() * 1.5))))
