# Brick Breaker 2D Arcade Game

An interactive 2D arcade Brick Breaker game developed using Python and Pygame, designed with a modular, object-oriented architecture.

---

## 1. Project Overview
This project is an implementation of the classic arcade breakout concept where a player controls a horizontal paddle to bounce a ball into a destructible wall of colored bricks. The game integrates real-time collision detection, dynamic velocity scaling, paddle deflection physics, and a full game-state management loop (playing, losing lives, game over, and victory).

---

## 2. Features
- **Dynamic Deflection Mechanics**: Ball rebound angles vary proportionally depending on the impact point on the paddle surface.
- **Progressive Difficulty**: Ball velocity accelerates incrementally by 4% upon brick destructions up to a defined velocity cap.
- **Mouse-Driven Controls**: Low-latency horizontal paddle movement constrained directly to the window boundaries.
- **Game State Flow**: Tracks player score (+10 points per brick) and 3-life endurance, triggering dedicated Game Over and Victory screens with one-click restart capability.
- **Modular OOP Architecture**: Decoupled design with dedicated modules for display configurations, paddle, ball physics, and wall management.

---

## 3. Technologies & Tools Used
- **Programming Language**: Python 3.9+
- **Game Framework**: Pygame 2.5+
- **Version Control**: Git & GitHub

---

## 4. Project Structure
```text
brick-breaker/
├── README.md           # Project documentation and instructions
├── statement.md        # Problem statement, scope, and high-level features
├── requirements.txt    # Python library dependencies
├── config.py           # Window dimensions, physics constants, and color palette
├── paddle.py           # Paddle entity logic, boundaries, and rendering
├── ball.py             # Ball kinematic update, boundary bouncing, and collisions
├── wall.py             # Brick grid generation, layout, and draw routines
└── main.py             # Game loop orchestration, event listening, and state flow
