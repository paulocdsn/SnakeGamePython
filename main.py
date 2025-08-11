# main.py
# Ponto de entrada do jogo. Aqui o jogador escolhe a dificuldade e o jogo é iniciado com curses.wrapper
import curses
from game import game_loop
from utils import select_difficulty

if __name__ == '__main__':
    game_speed = select_difficulty()  # Define o tempo de resposta do jogo
    curses.wrapper(game_loop, game_speed)  # Inicializa a tela e executa o loop principal


    