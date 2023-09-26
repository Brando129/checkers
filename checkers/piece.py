# Imports
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GRAY, CROWN

# Piece class
class Piece:
    PADDING = 15
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        # if self.color == RED:
        #     self.direction = -1
        # else:
        #     self.direcetion = 1
        self.x = 0
        self.y = 0
        self.calcuate_pos()

    # Calculates piece position
    def calcuate_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # Makes a king
    def make_king(self):
        self.king = True

    # Draws the piece and outline of the piece
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    # Move piece
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calcuate_pos()

    def __repr__(self):
        return str(self.color)