import pygame
import time
import random

import constants
from player import Player
from enemy import Enemy
from laser import Laser

class Game:
    
    def __init__(self) -> None:
        
        # We create the game window 
        self.__window = pygame.display.set_mode(constants.WINDOW_SIZE)
        # We give the game window a name
        pygame.display.set_caption("Space Invaders")
        
        # We load the background image
        self.__backgroud = pygame.image.load("assets/background.png")
        # We scale the background to fit the window
        self.__backgroud = pygame.transform.scale(self.__backgroud, constants.WINDOW_SIZE)
        
        # The object representing the player
        self.__player = Player()
        
        # The list of all enemies on the screen
        self.__enemies :list[Enemy] = []
        
        # The list of all lasers on the screen
        self.__lasers :list[Laser] = []
        
        # The main clock used to spawn enemies in
        self.__start_time = time.time()
        
        self.__font = pygame.font.Font("assets/akira.otf", 32)
        
    def run(self) -> None:
        
        # We set the state of the game as running
        self.__running = True
        
        # Main Game loop
        while self.__running:
            
            # We check player inputs
            self.handle_inputs()
            
            # We display the background on the screen
            self.__window.blit(self.__backgroud, (0, 0))
                        
            self.display_lives()   
                    
            # We set the player's position on the mouse cursor
            self.__player.set_position_on_cursor()
            
            # We handle all collisions
            self.handle_collisions()
            
            # We handle all the lasers logic
            self.handle_lasers()
            
            # We handle all te enemies logic
            self.handle_enemies()
            
            # We display the player on the screen
            self.display(self.__player)
  
            # We update the window to show our changes
            pygame.display.flip()

            # We check when was the last time we spawned an enemy and spawn new ones randomly
            if time.time() - self.__start_time > random.randint(1, 4):
                
                # We create a new enemy
                self.__enemies.append(Enemy())
                
                # We reset the clock
                self.__start_time = time.time()
            
            # We check if the player is dead
            if not self.__player.is_alive():
                # We stop the game
                self.__running = False
            
        # We quit the game and end the program
        pygame.quit()
        
    # We handle every input given by the player
    def handle_inputs(self) -> None:
        
        # We check each event that happened
        for event in pygame.event.get():
            
            # We check if the player pressed the close buton
            if event.type == pygame.QUIT:
                
                # We stop the game
                self.__running = False
            
            # We check if the player pressed the mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # We create a new laser
                self.__lasers.append(Laser(self.__player))
                
    # We display an object on the screen (the player or an enemy)
    def display(self, object :Player|Enemy|Laser) -> None:
        self.__window.blit(object.image, object.get_rect())
            
    # We handle all collisions
    def handle_collisions(self) -> None:
        
        self.update_lasers_list()
        self.update_enemies_list()
        
        # We loop through each laser
        for laser in self.__lasers:
            
            # We loop through each enemy per laser
            for enemy in self.__enemies:
                
                # We check if the laser intersects with the enemy (can be a laser shot by another enemy)
                if laser.get_rect().colliderect(enemy.get_rect()):
                    
                    # We change the laser's state
                    laser.is_alive = False
                    
                    # We kill the enemy
                    enemy.is_alive = False
                    
            # We check if the laser intersects with the player 
            if laser.get_rect().colliderect(self.__player.get_rect()):
                
                # We remove a life from the player
                self.__player.lives -= 1
                
                print("Laser hit")
                
                # We change the laser's state
                laser.is_alive = False
                
        self.update_enemies_list()        
            
        for enemy in self.__enemies:
            
            # We check if the enemy intersects with the player
            if enemy.get_rect().colliderect(self.__player.get_rect()):
                
                # We remove a life from the player
                self.__player.lives -= 1
                
                print("Enemy hit")
                
                # We kill the enemy
                enemy.is_alive = False
                
    def display_lives(self) -> None:
        
        text = self.__font.render(str(self.__player.lives) + "/3", True, (255, 0, 0))
        
        self.__window.blit(text, (constants.WINDOW_WIDTH - (constants.WINDOW_WIDTH // 8), 20))
        
    def update_enemies_list(self) -> None:
        
        new_enemies_list = []
        
        for enemy in self.__enemies:
            
            if enemy.is_alive:
                
                new_enemies_list.append(enemy)
        
        self.__enemies = new_enemies_list
                
    def update_lasers_list(self) -> None:
        
        new_lasers_list = []
        
        for laser in self.__lasers:
            
            if laser.is_alive:
                
                new_lasers_list.append(laser)
                
        self.__lasers = new_lasers_list
    
    # We handle all te enemies logic
    def handle_enemies(self) -> None:
        
        self.update_enemies_list()
        
        for enemy in self.__enemies:
            
            if enemy.is_on_screen():
                
                enemy.move_down()
                
                self.display(enemy)
                
                if enemy.can_shoot():
                    
                    self.__lasers.append(Laser(enemy))
            
            else:
                
                self.__player.lives -= 1
                
                enemy.is_alive = False
                
    # We handle all the lasers logic
    def handle_lasers(self) -> None:
        
        self.update_lasers_list()
        
        for laser in self.__lasers:
            
            if laser.is_on_screen():
                
                laser.move()
                
                self.display(laser)
                
            else:
                
                laser.is_alive = False