import pygame

from menu import Menu
from game import Game

if __name__ == "__main__":
 
    pygame.init()
    
    menu = Menu()
    
    menu.display()
        
    game = Game(menu.window)

    # We start the game
    game.run()
    
    # We quit the game and end the program
    pygame.quit()