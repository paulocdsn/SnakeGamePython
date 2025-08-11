# funções de movimentação, colisão, direção
# engine.py
# Lógica do movimento, colisões e geração de fruta
import curses
import random

def get_new_direction(window, timeout):
    """Captura tecla pressionada para mudar direção."""
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
        return direction
    return None

def direction_is_opposite(direction, current_direction):
    """Impede que a cobra vire 180 graus sobre si mesma."""
    opposites = {
        curses.KEY_UP: curses.KEY_DOWN,
        curses.KEY_DOWN: curses.KEY_UP,
        curses.KEY_LEFT: curses.KEY_RIGHT,
        curses.KEY_RIGHT: curses.KEY_LEFT
    }
    return opposites.get(direction) == current_direction

def move_snake(snake, direction, snake_eat_fruit):
    head = snake[0].copy()
    move_actor(head, direction)
    snake.insert(0, head)
    if not snake_eat_fruit:
        snake.pop()

def move_actor(actor, direction):
    if direction == curses.KEY_UP:
        actor[0] -= 1
    elif direction == curses.KEY_DOWN:
        actor[0] += 1
    elif direction == curses.KEY_LEFT:
        actor[1] -= 1
    elif direction == curses.KEY_RIGHT:
        actor[1] += 1

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(head, window)

def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    return (
        actor[0] <= 0 or actor[0] >= height - 1 or
        actor[1] <= 0 or actor[1] >= width - 1
    )

def snake_hit_itself(snake):
    head = snake[0]
    return head in snake[1:]

def snake_hit_fruit(snake, fruit):
    return fruit in snake

def get_new_fruit(window, snake):
    """
    Gera uma nova fruta fora da cobra.
    Repete até encontrar uma posição livre.
    """
    height, width = window.getmaxyx()
    while True:
        fruit = [random.randint(1, height - 2), random.randint(1, width - 2)]
        if fruit not in snake:
            return fruit
