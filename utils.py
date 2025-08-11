# funções auxiliares (ex: select_difficulty)
# utils.py
# Funções auxiliares, como seleção de dificuldade

def select_difficulty():
    """
    Solicita ao usuário a dificuldade (1 a 5) e retorna o tempo de resposta do jogo.
    """
    difficulty = {
        '1': 1000,  # Mais fácil
        '2': 500,
        '3': 150,
        '4': 90,
        '5': 35    # Mais difícil (cobra mais rápida)
    }
    while True:
        answer = input('Selecione a dificuldade de 1 a 5: ')
        game_speed = difficulty.get(answer)
        if game_speed is not None:
            return game_speed
        print('Escolha a dificuldade de 1 a 5 válida.')