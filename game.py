# lógica principal do jogo
# game.py
# Contém a função principal do jogo e o controle de fluxo do loop

import curses
import time
from render import draw_screen, draw_snake, draw_actor
from engine import (
    get_new_direction,
    direction_is_opposite,
    move_snake,
    snake_hit_border,
    snake_hit_itself,
    snake_hit_fruit,
    get_new_fruit
)

def game_loop(window, game_speed):
    curses.curs_set(0)
    snake = [[10, 15], [9, 15], [8, 15], [7, 15]]
    fruit = get_new_fruit(window, snake)
    current_direction = curses.KEY_DOWN
    snake_eat_fruit = False
    score = 0
    paused = False

    while True:
        draw_screen(window, score)
        draw_snake(snake, window)
        draw_actor(fruit, window, char=curses.ACS_DIAMOND)

        if paused:
            window.timeout(-1)  # espera indefinidamente por uma tecla (pausa real)
        else:
            window.timeout(game_speed)  # timeout normal do jogo

        direction = window.getch()

        if direction == ord('p') or direction == ord('P'):
            paused = not paused
            if paused:
                window.addstr(0, 20, "[PAUSADO]")
                window.refresh()
            else:
                window.addstr(0, 20, "         ")  # limpa texto da pausa
                window.refresh()
            continue

        if paused:
            continue  # ignora o resto do loop se estiver pausado

        if direction == -1 or direction_is_opposite(direction, current_direction):
            direction = current_direction

        move_snake(snake, direction, snake_eat_fruit)

        if snake_hit_border(snake, window) or snake_hit_itself(snake):
            break

        if snake_hit_fruit(snake, fruit):
            snake_eat_fruit = True
            fruit = get_new_fruit(window, snake)
            score += 1
        else:
            snake_eat_fruit = False

        current_direction = direction

    finish_game(score, window)


def finish_game(score, window):
    """Mostra mensagem de fim de jogo."""
    height, width = window.getmaxyx()
    s = f'Você perdeu! Coletou {score} frutas!'
    y = height // 2
    x = (width - len(s)) // 2
    window.addstr(y, x, s)
    window.refresh()
    time.sleep(4)
