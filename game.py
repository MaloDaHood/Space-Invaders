import pygame

from player import Player
from enemy import Enemy
from laser import Laser

class Game:
    
    def __init__(self) -> None:
        
        # We create the game window 
        self.window = pygame.display.set_mode((800, 800))
        # We give the game window a name
        pygame.display.set_caption("Space Invaders")
        
        # We load the background image
        self.backgroud = pygame.image.load("assets/background.png")
        # We scale the background to fit the window
        self.backgroud = pygame.transform.scale(self.backgroud, self.window.get_size())
        
        self.player = Player()
        
        self.enemies :list[Enemy] = []
        
        self.lasers :list[Laser] = []
        
    def run(self) -> None:
        
        # We set the state of the game as running
        self.running = True
        
        # Main Game loop
        while self.running:
            
            # We check player inputs
            self.handle_inputs()
            
            # We display the background on the screen
            self.window.blit(self.backgroud, (0, 0))
            
            # We set the player's position on the mouse cursor
            self.player.set_position_on_cursor()
            
            for enemy in self.enemies:
                
                # We make each enemy move each frame
                enemy.move_down()
            
                # We display each enemy on the screen
                self.display(enemy)
                
            for laser in self.lasers:
                
                # We make each laser move each frame
                laser.move()
                
                # We display each laser on the screen
                self.display(laser)
            
            # We display the player on the screen
            self.display(self.player)
            
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
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.lasers.append(Laser(self.player))
                
    # We display an object on the screen (the player or an enemy)
    def display(self, object :Player|Enemy|Laser) -> None:
        self.window.blit(object.get_image(), object.get_position())