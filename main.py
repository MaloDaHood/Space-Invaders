import pygame

from game import Game

if __name__ == "__main__":
 
    pygame.init()
    game = Game()

    # We start the game
    game.run()