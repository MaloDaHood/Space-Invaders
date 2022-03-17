import random

WINDOW_WIDTH = WINDOW_HEIGHT = 1000
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

COLORS = ["R", "G", "B"]
RED = (255, 0, 0)
BLACK = (0, 0, 0)

LASER_SPEED = WINDOW_WIDTH // 125

FLYING_SPEED = 0
    
SHOOTING_SPEED = 0

if WINDOW_HEIGHT < 800:
    
    FLYING_SPEED = 1
    
    SHOOTING_SPEED = random.choice([1, 1, 1.5])
    
else:
    
    FLYING_SPEED = random.randint(1, 3)
    
    SHOOTING_SPEED = random.choice([0.5, 1, 1, 1.5])

PLAYER_LIVES = 5
EARTH_LIVES = 10

EARTH_HEIGHT = WINDOW_HEIGHT // 10

MENU_FONT_SIZE = WINDOW_WIDTH // 20
GAME_FONT_SIZE = WINDOW_WIDTH // 30