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
        
        # We create a rectangle on the cursor to track it
        self.__cursor = pygame.Rect(pygame.mouse.get_pos(), (1, 1))
        
        # We create a rectangle representing the play button
        self.__play_button = pygame.Rect((constants.WINDOW_WIDTH // 4, constants.WINDOW_HEIGHT // 4), (constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 8))
        
        # We create a rectangle representing the quit button
        self.__quit_button = pygame.Rect((constants.WINDOW_WIDTH // 4, constants.WINDOW_HEIGHT - (constants.WINDOW_HEIGHT // 2)), (constants.WINDOW_WIDTH // 2, constants.WINDOW_HEIGHT // 8))
        
        # We load the font
        self.__font = pygame.font.Font("assets/akira.otf", constants.MENU_FONT_SIZE)
        
    def display(self) -> int:
        
        # Main loop
        while self.__running:
            
            # We display the background to the screen
            self.window.blit(self.__backgroud, (0, 0))
            
            # We update the cursor's position
            self.__cursor.topleft = pygame.mouse.get_pos()
                        
            # We display the play button to the screen
            pygame.draw.rect(self.window, constants.RED, self.__play_button, 2)
            
            # We display the quit button to the screen
            pygame.draw.rect(self.window, constants.RED, self.__quit_button, 2)
            
            # We display all the text to the screen
            self.display_text()
            
            # We get the player's input
            input = self.handle_inputs()
            
            # We check if the player pressed one of the buttons
            if input != 0:
                
                # We return what the player chose
                return input
            
            # We update the window to show the modifications
            pygame.display.flip()
            
        # Program shouldn't get here
        return -1
            
    # We handle every input given by the player and return 0 if no input was received, 1 if the player wants to play or -1 if he wants to exit the game
    def handle_inputs(self) -> int:
        
        # We check each event that happened
        for event in pygame.event.get():
            
            # We check if the player pressed the close buton
            if event.type == pygame.QUIT:
                
                return -1
            
            # We check if the player pressed the mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # We check if the player clicked the play button
                if self.__cursor.colliderect(self.__play_button):
                    
                    return 1
                
                # We check if the player clicked the quit button
                if self.__cursor.colliderect(self.__quit_button):
                    
                    return -1
                
        return 0
            
    # We display all the text on the window
    def display_text(self) -> None:
        
        # We set the text to what we need for the play button
        text = self.__font.render("PLAY", True, constants.RED)
        
        # We display the text at the right coordinates
        self.window.blit(text, (self.__play_button.x + ((constants.WINDOW_WIDTH // 4) - (text.get_width() // 2)) , self.__play_button.y + ((constants.WINDOW_HEIGHT // 8) - (text.get_height() * 1.75))))

        # We set the text to what we need for the quit button
        text = self.__font.render("QUIT", True, constants.RED)
        
        # We display the text at the right coordinates
        self.window.blit(text, (self.__quit_button.x + ((constants.WINDOW_WIDTH // 4) - (text.get_width() // 2)) , self.__quit_button.y + ((constants.WINDOW_HEIGHT // 8) - (text.get_height() * 1.75))))
