import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR
from paddle import Paddle
from ball import Ball
from wall import Wall

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brick Breaker")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 28)
    big_font = pygame.font.Font(None, 44)
    small_font = pygame.font.Font(None, 22)

    paddle = Paddle()
    ball = Ball()
    wall = Wall()

    score = 0
    lives = 3
    game_over = False
    game_won = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                paddle.move(event.pos[0])
            elif event.type == pygame.MOUSEBUTTONDOWN and (game_over or game_won):
                wall.build()
                ball.reset()
                score = 0
                lives = 3
                game_over = False
                game_won = False

        if not game_over and not game_won:
            ball.update()
            ball.handle_wall_collision()
            ball.handle_paddle_collision(paddle)
            score += ball.handle_brick_collision(wall)

            if ball.y > SCREEN_HEIGHT:
                lives -= 1
                if lives <= 0:
                    game_over = True
                else:
                    ball.reset()

            if len(wall.bricks) == 0:
                game_won = True

        screen.fill(BG_COLOR)
        wall.draw(screen)
        paddle.draw(screen)
        if not game_over:
            ball.draw(screen)

        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (15, 12))
        screen.blit(font.render(f"Lives: {lives}", True, (255, 120, 120)), (SCREEN_WIDTH - 95, 12))

        if game_over:
            text = big_font.render("Game Over!", True, (240, 70, 70))
            sub = small_font.render("Click anywhere to restart", True, (180, 180, 180))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10)))
            screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)))
        elif game_won:
            text = big_font.render("You Win!", True, (80, 230, 80))
            sub = small_font.render("Click anywhere to play again", True, (180, 180, 180))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10)))
            screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()