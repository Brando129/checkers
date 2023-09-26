# Imports
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
# from checkers.board import Board
from checkers.game import Game

# Set up the game display
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        game.update()

    pygame.quit()

main()