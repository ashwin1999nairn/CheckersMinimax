import pygame
from draughts.checkers_board import Board
from .define import MAC, HUMAN, GREEN, BOX_SIZE

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = HUMAN
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        stone = self.board.get_stone(row, col)
        if stone != 0 and stone.color == self.turn:
            self.selected = stone
            self.valid_moves = self.board.get_valid_moves(stone)
            return True

        return False

    def _move(self, row, col):
        stone = self.board.get_stone(row, col)
        if self.selected and stone == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * BOX_SIZE + BOX_SIZE // 2, row * BOX_SIZE + BOX_SIZE // 2), 15)

    def change_turn(self):
        self.valid_moves = []
        if self.turn == HUMAN:
            self.turn = MAC
        else:
            self.turn = HUMAN

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()