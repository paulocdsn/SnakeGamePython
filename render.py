# funções de desenho (draw_actor, draw_screem, etc)
# render.py
# Funções responsáveis pela exibição gráfica da cobra, fruta e placar

def draw_screen(window, score):
    """
    Limpa a tela, desenha a borda e mostra a pontuação atual.
    """
    window.clear()
    window.border(0)
    window.addstr(0, 2, f' Pontuação: {score} ')

def draw_snake(snake, window):
    """
    Desenha a cobra na tela. Cabeça é '@', corpo é 's'.
    """
    head = snake[0]
    draw_actor(head, window, "@")
    for part in snake[1:]:
        draw_actor(part, window, 's')

def draw_actor(actor, window, char):
    """
    Desenha um caractere (cobra ou fruta) na posição do ator.
    """
    window.addch(actor[0], actor[1], char)
