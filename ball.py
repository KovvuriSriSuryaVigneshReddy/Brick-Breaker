import pygame
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, BALL_RADIUS, BALL_INITIAL_SPEED_X,
    BALL_INITIAL_SPEED_Y, MAX_SPEED, BALL_COLOR
)

class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2 + 50
        self.vx = BALL_INITIAL_SPEED_X if random.random() > 0.5 else -BALL_INITIAL_SPEED_X
        self.vy = BALL_INITIAL_SPEED_Y

    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def handle_wall_collision(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.vx = -self.vx
        if self.y - self.radius <= 0:
            self.vy = abs(self.vy)

    def handle_paddle_collision(self, paddle):
        if self.vy > 0 and paddle.rect.collidepoint(self.x, self.y + self.radius):
            self.vy = -abs(self.vy)
            center = paddle.x + paddle.w / 2
            offset = (self.x - center) / (paddle.w / 2)
            self.vx = offset * 6
            if abs(self.vx) < 1:
                self.vx = 2 if self.vx >= 0 else -2

    def handle_brick_collision(self, wall):
        for b in wall.bricks:
            if self.rect.colliderect(b):
                wall.bricks.remove(b)
                dx = abs(self.x - b.centerx) * b.height
                dy = abs(self.y - b.centery) * b.width
                if dx > dy:
                    self.vx = -self.vx
                else:
                    self.vy = -self.vy

                if abs(self.vx) < MAX_SPEED:
                    self.vx *= 1.04
                if abs(self.vy) < MAX_SPEED:
                    self.vy *= 1.04
                return 10
        return 0

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), self.radius)