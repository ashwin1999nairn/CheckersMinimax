import pygame
from copy import deepcopy

from draughts.define import MAC


HUMAN = (255, 255, 255)
MAC = (106, 2, 2)


def minimax(pos, dep, max_player, game): # Position is passed to pass the board object 
    if dep == 0 or pos.winner() != None: #dep is depth which will be decreased since it is a recursive call
        return pos.eval(), pos           # max_player is a boolean expression which true maximises and vice-versa
# base case of recursion
    if max_player:
        max_eval = float('-inf')
        best_move = None
        for move in all_moves(pos, MAC, game):
            eval = minimax(move, dep - 1, False, game)[0]
            max_eval = max(max_eval, eval)
            if max_eval == eval:
                best_move = move

        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in all_moves(pos, HUMAN, game):
            eval = minimax(move, dep - 1, True, game)[0]
            min_eval = min(min_eval, eval)
            if min_eval == eval:
                best_move = move

        return min_eval, best_move


def sim_move(stone, move, board, game, skip): # Simulates all of the valid moves
    board.move(stone, move[0], move[1])
    if skip:
        board.remove(skip)     # If we jumped over a piece, the piece is removed and new board is updated

    return board


def all_moves(board, color, game): # makes a list of all the possible boards according to all the valid moves
    moves = []

    for stone in board.all_stones(color):
        valid_moves = board.get_valid_moves(stone)
        for move, skip in valid_moves.items():
            #draw_moves(game, board, stone)
            temp_board = deepcopy(board)  #Temporary boards for every valid move
            temp_stone = temp_board.get_stone(stone.row, stone.col)
            new_board = sim_move(temp_stone, move, temp_board, game, skip)
            moves.append(new_board)  

    return moves # Will run through the above algorithm and accordingly select best move

def draw_moves(game, board, stone):
    valid_moves = board.get_valid_moves(stone)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (stone.x, stone.y), 50 ,5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)