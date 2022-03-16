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
        
        self.__earth = pygame.image.load("assets/earth.png")
        
        self.__earth = pygame.transform.scale(self.__earth, (constants.WINDOW_WIDTH, constants.EARTH_HEIGHT))
        
        self.__earth_lives = constants.EARTH_LIVES
        
        # The object representing the player
        self.__player = Player()
        
        # The list of all enemies on the screen
        self.__enemies :list[Enemy] = []
        
        # The list of all lasers on the screen
        self.__lasers :list[Laser] = []
        
        # The main clock used to spawn enemies in
        self.__start_time = time.time()
        
        # We load the font
        self.__font = pygame.font.Font("assets/akira.otf", 32)
        
        # We make the cursor invisible
        pygame.mouse.set_visible(False)
        
        # We set the cursor's position to the center of the window
        pygame.mouse.set_pos((constants.WINDOW_WIDTH / 2, constants.WINDOW_HEIGHT / 2))
        
    def run(self) -> None:
        
        # We set the state of the game as running
        self.__running = True
        
        # Main Game loop
        while self.__running:
            
            # We check player inputs
            self.handle_inputs()
            
            # We display the background on the screen
            self.__window.blit(self.__backgroud, (0, 0))
            
            self.__window.blit(self.__earth, (0, constants.WINDOW_HEIGHT - constants.EARTH_HEIGHT))
                        
            # We display the number of lives the player has left
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
            if not self.__player.is_alive() or self.__earth_lives < 1:
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
              
    # We display the number of lives the player and the earth have left  
    def display_lives(self) -> None:
        
        # We define the text we want to dispay
        text = self.__font.render(str(self.__player.lives) + "/" + str(constants.PLAYER_LIVES), True, (255, 0, 0))
        
        # We display it to the sreen
        self.__window.blit(text, (constants.WINDOW_WIDTH - (constants.WINDOW_WIDTH // 8), 20))
        
        text = self.__font.render(str(self.__earth_lives) + "/" + str(constants.EARTH_LIVES), True, (255, 0, 0))
        
        self.__window.blit(text, (constants.WINDOW_WIDTH - (constants.WINDOW_WIDTH // 8), constants.WINDOW_HEIGHT - constants.EARTH_HEIGHT))
        
    # We return an updated version of the given list (we remove the dead enemies or lasers)
    def update(self, origin_list :list) -> list:
        
        new_list = []
        
        # We loop through each object in the list
        for element in origin_list:
            
            # We check if the object has .is_alive == True
            if element.is_alive:
                
                # We add the object to the new list
                new_list.append(element)
                
        # We return the new list containing only living objects
        return new_list    
        
    # We handle all collisions
    def handle_collisions(self) -> None:
        
        # We update both lists
        self.__enemies = self.update(self.__enemies)
        self.__lasers = self.update(self.__lasers)
        
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
                                
                # We change the laser's state
                laser.is_alive = False
                
        # We update the enemies list once again to take into account what we might have modified right above
        self.__enemies = self.update(self.__enemies)   
            
        # We loop again through the enemies (needed for stability)
        for enemy in self.__enemies:
            
            # We check if the enemy intersects with the player
            if enemy.get_rect().colliderect(self.__player.get_rect()):
                
                # We remove a life from the player
                self.__player.lives -= 1
                                
                # We kill the enemy
                enemy.is_alive = False
                
    # We handle all the lasers logic
    def handle_lasers(self) -> None:
        
        # We update the lasers list
        self.__lasers = self.update(self.__lasers)
        
        # We loop through each laser in the list
        for laser in self.__lasers:
            
            # We check if the laser is still on the screen
            if laser.is_on_screen():
                
                # We make it move
                laser.move()
                
                # We display it to the screen
                self.display(laser)
                
            else:
                # Otherwise we set it as dead
                laser.is_alive = False
                
    # We handle all the enemies logic
    def handle_enemies(self) -> None:
                
        # We update the enemies list
        self.__enemies = self.update(self.__enemies)
        
        # We loop through each enemy in the list
        for enemy in self.__enemies:
            
            # We check if the enemy is still on the screen
            if enemy.is_on_screen():
                
                # We make it move
                enemy.move_down()
                
                # We display it to the screen
                self.display(enemy)
                
                # We check if the enemy is able to shoot
                if enemy.can_shoot():
                    
                    # We create a new laser from the enemy's data
                    self.__lasers.append(Laser(enemy))
            
            else:
                # Otherwise we remove a life from the player
                self.__earth_lives -= 1
                
                # And we set the enemy as dead
                enemy.is_alive = False
                
    # We display an object on the screen (the player, an enemy or a laser)
    def display(self, object :Player|Enemy|Laser) -> None:
        
        # We display the object
        self.__window.blit(object.image, object.get_rect())
