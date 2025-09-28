# Space Invaders

This is a Python-based Space Invaders game using Pygame. The game features player and enemy sprites, bullets, scoring, sound effects, and increasing difficulty as you score points.

## Features
- Player-controlled spaceship with left and right movement.
- Enemies move horizontally and descend gradually.
- Bullet firing to eliminate enemies.
- Score tracking and display.
- Game over condition when an enemy reaches the player.
- Background music and sound effects for firing and collisions.
- Gradually increasing enemy speed as the player scores.

## Installation
1. Make sure Python and Pygame are installed:
```bash
pip install pygame
```

2. Place the following assets in the project directory:
- `background.jpg` - background image
- `background.wav` - background music
- `ufo.png` - game icon
- `space-invaders.png` - player sprite
- `enemy.png` - enemy sprite
- `bullet.png` - bullet sprite
- `laser.wav` - bullet sound
- `explosion.wav` - enemy hit sound
- `curb.wav` - game over sound

## Usage
Run the game using:
```bash
python space_invaders.py
```

- Use LEFT and RIGHT arrow keys to move the player.
- Press SPACE to fire bullets.
- Avoid enemy collisions to prevent game over.
- The game will increase enemy speed every 10 points.

## How it Works
- The game initializes Pygame and sets up the screen, background, and music.
- The player and enemies are represented as images on the screen.
- Player can move left or right and shoot bullets.
- Enemies move horizontally and drop down when hitting screen boundaries.
- Collision detection is used to check if the bullet hits an enemy or if an enemy reaches the player.
- Score increments with each enemy destroyed.
- The game loop continuously updates the screen and checks for player inputs and collisions.

## Controls
- **Left Arrow**: Move left
- **Right Arrow**: Move right
- **Space**: Fire bullet

## Game Over
- When an enemy collides with the player, the game stops.
- A 'GAME OVER' message is displayed.
- Background music changes to indicate game over.

## Notes
- Adjust `enemy_speed` and `bullet_speed` values to modify difficulty.
- Sound and image files must be correctly named and present in the same folder as the script.

Enjoy playing Space Invaders UwU!

