import pygame
import time
import random

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
        
        # The object representing the player
        self.player = Player()
        
        # The list of all enemies on the screen
        self.enemies :list[Enemy] = []
        
        # The list of all lasers on the screen
        self.lasers :list[Laser] = []
        
        # The main clock used to spawn enemies in
        self.start_time = time.time()
        
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
            
            # We handle all collisions
            self.handle_collisions()
            
            # We handle all the lasers logic
            self.handle_lasers()
            
            # We handle all te enemies logic
            self.handle_enemies()
            
            # We display the player on the screen
            self.display(self.player)
  
            # We update the window to show our changes
            pygame.display.flip()

            # We check when was the last time we spawned an enemy and spawn new ones randomly
            if time.time() - self.start_time > random.randint(1, 4):
                
                # We create a new enemy
                self.enemies.append(Enemy())
                
                # We reset the clock
                self.start_time = time.time()
            
            # We check if the player is dead
            if not self.player.is_alive():
                # We stop the game
                self.running = False
            
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
            
            # We check if the player pressed the mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # We create a new laser
                self.lasers.append(Laser(self.player))
                
    # We display an object on the screen (the player or an enemy)
    def display(self, object :Player|Enemy|Laser) -> None:
        self.window.blit(object.get_image(), object.get_rect())
        
    # We handle all te enemies logic
    def handle_enemies(self) -> None:
        
        # We create a list containing all the indexes of dead enemies
        dead_indexes = []
        
        # We loop through the entire list of enemies
        for i in range(len(self.enemies)):
            
            # We check if the enemy is alive and is on the screen
            if self.enemies[i].is_alive() and self.enemies[i].is_on_screen():
                
                # We make each enemy move each frame
                self.enemies[i].move_down()
            
                # We display each enemy on the screen
                self.display(self.enemies[i])
                
                # We check if the enemy can shoot
                if self.enemies[i].can_shoot():
                    
                    # We create a new laser from the enemy
                    self.lasers.append(Laser(self.enemies[i]))
            
            # We check if the enemy is alive and not on the screen
            elif self.enemies[i].is_alive() and not self.enemies[i].is_on_screen():
                
                # We make the player loose onr life 
                self.player.loose_life()
                
                # We add the enemy's index to the list of dead indexes
                dead_indexes.append(i)
                
            else:
                # We add the enemy's index to the list of dead indexes
                dead_indexes.append(i)
        
        # We loop through each index in the list 
        for index in dead_indexes:
            # We remove the list entry at each one of the indexes
            self.enemies.pop(index)
                
    # We handle all the lasers logic
    def handle_lasers(self) -> None:
        
        # We create a list containing all the indexes of dead lasers
        dead_indexes = []
        
        # We loop through the entire list of lasers
        for i in range(len(self.lasers)):
        
            # We check if the laser is on the screen and if it hasn't touched an enemy
            if self.lasers[i].is_on_screen() and not self.lasers[i].has_touched_enemy():
                
                # We make each enemy move each frame
                self.lasers[i].move()
            
                # We display each enemy on the screen
                self.display(self.lasers[i])
                
            else:
                # We add the laser's index to the list of dead indexes
                dead_indexes.append(i)
            
        # We loop through each index in the list 
        for index in dead_indexes:
            # We remove the list entry at each one of the indexes
            self.lasers.pop(index)
            
    # We handle all collisions
    def handle_collisions(self) -> None:
        
        # We loop through each laser
        for laser in self.lasers:
            
            # We loop through each enemy per laser
            for enemy in self.enemies:
                
                # We check if the laser intersects with the enemy (can be a laser shot by another enemy)
                if laser.get_rect().colliderect(enemy.get_rect()):
                    
                    # We change the laser's state
                    laser.touched_enemy()
                    
                    # We kill the enemy
                    enemy.die()
                
                # We check if the enemy intersects with the player
                if enemy.get_rect().colliderect(self.player.get_rect()):
                    
                    # We remove a life from the player
                    self.player.loose_life()
                    
                    # We kill the enemy
                    enemy.die()

            # We check if the laser intersects with the player 
            if laser.get_rect().colliderect(self.player.get_rect()):
                
                # We remove a life from the player
                self.player.loose_life()
                
                # We change the laser's state
                laser.touched_enemy()