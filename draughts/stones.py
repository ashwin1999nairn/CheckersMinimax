import pygame
from .define import HUMAN, MAC, BOX_SIZE, BLUE, KING

class Stone:
    PADDING = 10
    OUTLINE = 3

    def __init__(self, row ,col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def trans_king(self):
        self.king = True

    def calc_pos(self):
        self.x = BOX_SIZE * self.col + BOX_SIZE // 2
        self.y = BOX_SIZE * self.row + BOX_SIZE // 2

    def draw(self, win):
        rad = BOX_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, BLUE, (self.x, self.y), rad + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), rad)
        if self.king:
            win.blit(KING, (self.x - KING.get_width()//2, self.y - KING.get_height()//2))

    def move(self, row , col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)