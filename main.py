import pygame
import random

pygame.init()
window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Space Invaders")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()