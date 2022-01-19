import pygame

BREADTH, HEIGHT = 625, 625
ROWS, COLS = 8, 8
BOX_SIZE = BREADTH//COLS
# Colour codes for, outline and valid moves #
HUMAN = (255, 255, 255)
MAC = (106, 2, 2)
BLACK = (0, 0, 0)
GREEN = (15, 234, 185)
BLUE = (255, 215, 0)

KING = pygame.transform.scale(pygame.image.load('images/crown.png'), (45, 25))