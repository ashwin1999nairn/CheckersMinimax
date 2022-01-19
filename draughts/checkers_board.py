import pygame
from .stones import Stone
from .define import BLACK, ROWS, HUMAN, BOX_SIZE, COLS, MAC
# Intialising number of pieces for each human and machine #
class Board:
    def __init__(self):
        self.board = []
        self.mac_left = self.human_left = 12
        self.mac_kings = self.human_kings = 0
        self.create_board()
# making the entire design of the checkers board #
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS , 2):
                pygame.draw.rect(win, HUMAN, (row * BOX_SIZE, col * BOX_SIZE, BOX_SIZE, BOX_SIZE))

    def eval(self):
        return self.human_left - self.mac_left + (self.human_kings * 0.5 - self.mac_kings * 0.5)

    def all_stones(self, color):
        stones = []
        for row in self.board:
            for stone in row:
                if stone != 0 and stone.color == color:
                    stones.append(stone)
        return stones

    def move(self, stone, row ,col):
        self.board[stone.row][stone.col], self.board[row][col] = self.board[row][col], self.board[stone.row][stone.col]
        stone.move(row, col)

        if row == ROWS -1 or row == 0:
            stone.trans_king()
            if stone.color == MAC:
                self.human_kings += 1
            else:
                self.mac_kings += 1

    def get_stone(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in  range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Stone(row, col, MAC))
                    elif row > 4:
                        self.board[row].append(Stone(row, col, HUMAN))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                stone = self.board[row][col]
                if stone != 0:
                    stone.draw(win)

    def remove(self, stones):
        for stone in stones:
            self.board[stone.row][stone.col] = 0
            if stone != 0:
                if stone.color == HUMAN:
                    self.mac_left -= 1
                else:
                    self .human_left -=1

    def winner(self):
        if self.mac_left <= 0:
            return MAC
        elif self.human_left <= 0:
            return HUMAN
        return None

    def get_valid_moves(self, stone):
        moves = {}
        left = stone.col - 1
        right = stone.col + 1
        row = stone.row

        if stone.color == HUMAN or stone.king:
            moves.update(self._trav_left(row - 1, max(row - 3, -1), -1, stone.color, left))
            moves.update(self._trav_right(row - 1, max(row - 3, -1), -1, stone.color, right))
        if stone.color == MAC or stone.king:
            moves.update(self._trav_left(row + 1, min(row + 3, ROWS), 1, stone.color, left))
            moves.update(self._trav_right(row + 1, min(row + 3, ROWS), 1, stone.color, right))

        return moves

    def _trav_left(self, start, stop, step, color , left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._trav_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.update(self._trav_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def _trav_right(self, start, stop, step, color , right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._trav_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._trav_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
