import pygame
from config import SCREEN_WIDTH, PADDLE_W, PADDLE_H, PADDLE_Y, PADDLE_COLOR

class Paddle:
    def __init__(self):
        self.w = PADDLE_W
        self.h = PADDLE_H
        self.x = (SCREEN_WIDTH - self.w) // 2
        self.y = PADDLE_Y

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)

    def move(self, mouse_x):
        self.x = mouse_x - self.w // 2
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.w:
            self.x = SCREEN_WIDTH - self.w

    def draw(self, surface):
        pygame.draw.rect(surface, PADDLE_COLOR, self.rect, border_radius=5)