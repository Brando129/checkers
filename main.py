# Imports
import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

# Set up the game display
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    # Event loop
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()