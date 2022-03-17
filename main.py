import pygame

from menu import Menu
from game import Game

if __name__ == "__main__":
 
    pygame.init()
    
    menu = Menu()
    
    # We check if the player wants to play
    if menu.display() == 1:
        
        # We pass the same window as the menu to the game
        game = Game(menu.window)

        # We start the game
        game.run()
    
    # We quit the game and end the program
    pygame.quit()