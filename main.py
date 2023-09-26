# Imports
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
# from checkers.board import Board
from checkers.game import Game
from minimax.algo import minimax

# Set up the game display
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# Determines which box the user is clicking
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()
    # board = Board()
    game = Game(WIN)

    # Event loop
    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner()) # Make this more interesting
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # piece = board.get_piece(row, col)
                # board.move(piece, 4, 3)
                game.select(row, col)


        game.update()

    pygame.quit()

main()