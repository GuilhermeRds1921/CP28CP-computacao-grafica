def draw_square(width, height, size):
    # Inicializa a "tela" (matriz) com espaços em branco
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Calcula as coordenadas do quadrado centralizado
    start_x = (width - size) // 2
    start_y = (height - size) // 2

    # Loop pelas linhas da "tela"
    for y in range(start_y, start_y + size):
        # Desenha a linha do quadrado
        for x in range(start_x, start_x + size):
            screen[y][x] = '#'

    # Imprime a "tela" resultante
    for row in screen:
        print(''.join(row))


# Entrada do usuário para o tamanho do quadrado e o tamanho da tela
width = int(input("Digite a largura da tela: "))
height = int(input("Digite a altura da tela: "))
size = int(input("Digite o tamanho do quadrado: "))

draw_square(width, height, size)