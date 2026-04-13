# MarioGame
Super Mario Bros (Python Project)

# Overview

This project is a simplified recreation of the classic Super Mario Bros game, developed using Python and the Pyxel library. It follows object-oriented programming (OOP) principles, focusing on clean structure, readability, and maintainability.

The game includes core mechanics such as player movement, enemies, collisions, scoring, and game states.

# Project Structure

The project is built using multiple classes and supporting files:

Main Components
- Main File
    - Entry point of the program
    - Initializes the game and runs Pyxel
    - Creates an instance of the Board class
- Board Class
    - Core game controller
    - Handles rendering, updates, collisions, and game state
    - Manages all game objects (Mario, enemies, platforms, coins)
- Mario Class
    - Represents the player
    - Handles movement (left, right, jump)
    - Contains unique behaviors separate from enemies
- Enemy Class (Parent Class)
    - Base class for all enemies and coins
    - Defines shared attributes and behavior
- Enemy Subclasses(Each has specific movement patterns and attributes)
    - Crab
    - Turtle
    - Fly
- Coin Class
    - Inherits from Enemy
    - Used for scoring
- Platform Class
    - Represents platforms in the game
    - Enables collision handling without hardcoding coordinates
- Constants File
    - Stores global values

# Game Mechanics

Control Mario, defeat enemies, collect coins, and survive as long as possible.

- Controls
    - Move Left / Right
    - Jump
    - Combine jump + movement for advanced control
- Interactions
    - Jump under enemies to flip them
    - Kick flipped enemies to eliminate them
    - Collect coins to increase score
- Lives System
    - Mario starts with limited lives
    - Losing all lives triggers Game Over
# Game Flow
1. Start Screen - Press space to begin
2. Gameplay
   - Enemies spawn randomly over time
   - Difficulty increases as the game progresses
3. Game Over
   - Display final score
   - Option to restart

# Key Methods

update() - Updates positions and states of all game objects

draw() - Renders all elements on screen

__check_all_collisions() - Handles: 
- Mario vs enemies
- Enemy vs enemy
- Mario vs coins

enemy_hit, enemy_stand_coll, kick_enemy - Handle combat interactions

# Algorithms & Logic
- Random enemy spawning with increasing difficulty
- Collision detection between all objects
- Gravity simulation for movement
- Game state management: "start_screen"; "game"; "game_over"

# Features
- Object-oriented design with inheritance and encapsulation
- Multiple enemy types with unique behaviors
- Dynamic difficulty progression
- Score tracking system
- Clean and modular code structure

# Technologies Used
- Python
- Pyxel (for graphics and game loop)
- GitHub (for collaboration)

# Challenges
- Implementing different enemy behaviors
- Managing collisions and interactions
- Simulating gravity and movement
- Structuring code efficiently across multiple classes

# Authors
Silvia Andreeva
Noa Dori
