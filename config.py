# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
FPS = 60

# Paddle settings
PADDLE_W = 80
PADDLE_H = 12
PADDLE_Y = SCREEN_HEIGHT - 40

# Ball settings
BALL_RADIUS = 6
BALL_INITIAL_SPEED_X = 4
BALL_INITIAL_SPEED_Y = -5
MAX_SPEED = 9

# Brick layout
ROWS = 6
COLS = 8
BRICK_H = 18
START_Y = 50

# Palette
BRICK_COLORS = [
    (231, 76, 60),   # red
    (230, 126, 34),  # orange
    (241, 196, 15),  # yellow
    (46, 204, 113),  # green
    (52, 152, 219),  # blue
    (155, 89, 182)   # purple
]
BG_COLOR = (25, 25, 35)
PADDLE_COLOR = (220, 220, 240)
BALL_COLOR = (255, 255, 255)