import pygame

from player import Player
from enemy import Enemy

class Game:
    
    def __init__(self) -> None:
        
        # We create the game window 
        self.window = pygame.display.set_mode((800, 800))
        # We give the game window a name
        pygame.display.set_caption("Space Invaders")
        
        # We load the background image
        self.backgroud = pygame.image.load("assets/background.png")
        # We scale the background to fit the window
        self.backgroud = pygame.transform.scale(self.backgroud, (800, 800))
        
    def run(self) -> None:
        
        # We initiate the different classes
        player = Player()
        enemy = Enemy()
        
        # We set the state of the game as running
        self.running = True
        
        # As long as the game is running
        while self.running:
            
            # We check player inputs
            self.handle_inputs()
            
            # We display the background on the screen
            self.window.blit(self.backgroud, (0, 0))
            
            # We set the player's position on the mouse cursor
            player.set_position_on_cursor()
            
            # We make the enemy move each frame
            enemy.move_down()
            
            # We display the enemy on the screen
            self.display(enemy)
            
            # We display the player on the screen
            self.display(player)
            
            # We update the window to show our changes
            pygame.display.flip()
        
        # We quit the game and end the program
        pygame.quit()
        
    # We handle every input given by the player
    def handle_inputs(self) -> None:
        
        # We check each event that happened
        for event in pygame.event.get():
            
            # We check if the player pressed the close buton
            if event.type == pygame.QUIT:
                
                # We stop the game
                self.running = False
                
    # We display an object on the screen (the player or an enemy)
    def display(self, object :Player|Enemy) -> None:
        self.window.blit(object.get_image(), object.get_position())