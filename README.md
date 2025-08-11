Snake Game in Python (Terminal)
This project is a classic Snake game implemented to run directly in the terminal using the curses library. It features smooth movement control, collision detection, random fruit generation, a scoring system, and multiple difficulty levels.

Project Structure
engine.py
Contains the core game logic: snake movement, collision checks (with walls and itself), direction control, and fruit generation in valid positions.

game.py
Manages the main game loop, updates the screen, reads player input, handles pausing, updates the snake’s position, and checks for game-over conditions.

render.py
Handles rendering the snake, fruit, game border, and score on the terminal screen.

utils.py
Contains helper functions, such as an interactive difficulty selector that controls the snake’s speed.

main.py
The program entry point. Initializes the curses interface and starts the game loop after the player selects a difficulty.

How to Play
Run python main.py in your terminal.

Choose a difficulty level (1 to 5).

Use the arrow keys to control the snake.

Press P to pause or resume the game.

Try to eat as many fruits as possible without hitting the walls or the snake’s own body.
