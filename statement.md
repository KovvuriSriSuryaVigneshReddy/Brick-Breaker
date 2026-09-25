# Project Statement: Brick Breaker Arcade

## 1. Problem Statement
Classic 2D arcade games serve as a fundamental benchmark for real-time physics engines, collision handling, and interactive user loop modeling. The goal of this project is to implement a robust, lightweight, object-oriented 2D Breakout/Brick-Breaker game in Python using Pygame, emphasizing clean architectural separation between physics, entity state, and rendering.

## 2. Scope of the Project
- Real-time mouse-controlled player movement and boundary containment.
- Dual-axis elastic ball rebound dynamics with dynamic angle deflection based on paddle impact offsets.
- Two-dimensional axis-aligned bounding box (AABB) collision detection against destructible brick layers.
- Life counter, score tracking, dynamic speed scaling, and game-state transitions (Play, Game Over, Victory).

## 3. Target Users
- Casual desktop arcade game players.
- Students and instructors evaluating real-time 2D game loops, state machines, and modular Python development.

## 4. High-Level Features
- **Dynamic Ball Deflection**: Ball rebound angles vary based on point of contact with the paddle.
- **Progressive Difficulty**: Ball velocity accelerates incrementally by 4% upon brick destructions up to a terminal cap.
- **Clean State Recovery**: Complete reset capabilities upon victory or loss without restarting the Python interpreter.
