import pygame
from config import SCREEN_WIDTH, ROWS, COLS, BRICK_H, START_Y, BRICK_COLORS

class Wall:
    def __init__(self):
        self.brick_w = (SCREEN_WIDTH - 20) // COLS
        self.bricks = []
        self.build()

    def build(self):
        self.bricks.clear()
        for r in range(ROWS):
            for c in range(COLS):
                x = 10 + c * self.brick_w
                y = START_Y + r * (BRICK_H + 3)
                rect = pygame.Rect(x, y, self.brick_w - 2, BRICK_H)
                self.bricks.append(rect)

    def draw(self, surface):
        for b in self.bricks:
            row_num = (b.y - START_Y) // (BRICK_H + 3)
            color = BRICK_COLORS[row_num % len(BRICK_COLORS)]
            pygame.draw.rect(surface, color, b, border_radius=3)