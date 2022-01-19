import pygame
from minimax.minimax import  minimax
from draughts.game import Game
from draughts.define import BREADTH, HEIGHT, BOX_SIZE, HUMAN, MAC

FPS = 90

WIN = pygame.display.set_mode((BREADTH, HEIGHT))
pygame.display.set_caption('Checkers with AI')

def get_row_col(pos): # Gets the current position of our mouse, selects the piece and can move our piece
    x, y = pos
    row = y // BOX_SIZE
    col = x // BOX_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == MAC:
            value, new_board = minimax(game.get_board(), 3, MAC, game)
            game.ai_move(new_board)

        if game.winner() != None:
            if game.winner() == HUMAN:
                print('HUMAN WINS!')
            elif game.winner() == MAC:
                print('MACHINE WINS!')
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: #This enables the mouse functionalities in the game
                pos = pygame.mouse.get_pos()
                row, col = get_row_col(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()
