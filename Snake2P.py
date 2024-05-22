import pygame
import random

pygame.init()

winner1 = False
winner2 = False

# Dimensiones del juego
width = 800
height = 600

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# la ventana
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Velocidad 
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10

# Fuentes para los textos
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Función para mostrar el puntaje
def show_score(score1, score2):
    score1_text = score_font.render("Player 1 Score: " + str(score1), True, green)
    score2_text = score_font.render("Player 2 Score: " + str(score2), True, blue)
    window.blit(score1_text, (10, 10))
    window.blit(score2_text, (10, 40))


def update_highscore(player, score1, score2):
    # Leer el archivo de highscore
    try:
        with open("highscorep1.txt", "r") as file:
            highscore1 = int(file.read())
    except FileNotFoundError:
        highscore1 = 0

    # Actualizar el highscore si el puntaje es mayor
    if score1 > highscore1:
        highscore1 = score1

    # Guardar el highscore en el archivo
    with open("highscorep1.txt", "w") as file:
        file.write(str(highscore1))

    # Mostrar el highscore en la ventana del juego
    highscore_text = score_font.render("Player 1 Highscore: " + str(highscore1), True, green)
    window.blit(highscore_text, (530, 10))

    try:
        with open("highscorep2.txt", "r") as file:
            highscore2 = int(file.read())
    except FileNotFoundError:
        highscore2 = 0
        # Actualizar el highscore si el puntaje es mayor
    if score2 > highscore2:
        highscore2 = score2
        # Guardar el highscore en el archivo
    with open("highscorep2.txt", "w") as file:
        file.write(str(highscore2))
        # Mostrar el highscore en la ventana del juego
    highscore_text = score_font.render("Player 2 Highscore: " + str(highscore2), True, blue)
    window.blit(highscore_text, (530, 40))



# Función para mostrar la serpiente
def draw_snake(snake_list, color):
    for x in snake_list:
        pygame.draw.rect(window, color, [x[0], x[1], snake_block, snake_block])




def game():
    game_over = False
    game_close = False
    winner1 = False
    winner2 = False

    # Posiciones iniciales 
    player1_x = width * 3 / 4
    player1_y = height / 2
    player2_x = width / 4 
    player2_y = height / 2

    # Velocidades iniciales
    player1_x_change = 0
    player1_y_change = 0
    player2_x_change = 0
    player2_y_change = 0

    # Tamaño inicial
    player1_length = 2
    player2_length = 2

    # Listas para guardar las posiciones de las serpientes
    player1_snake_list = []
    player2_snake_list = []

    # Posicion fruta
    fruit_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    fruit_y = round(random.randrange(0, height - snake_block) / 30.0) * 10


    while not game_over:

        while game_close:
            # Mostrar game over y opciones
            game_over_text = font_style.render("Game Over!", True, red)
            window.fill(black)
            restart_text = score_font.render("Press R to Restart or Q to Quit", True, white)
            window.blit(game_over_text, (width / 2 - 100, height / 2 - 50))
            window.blit(restart_text, (width / 2 - 150, height / 2))
            pygame.display.update()
            # Usar teclas en el Game Over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False


        if player1_length -2 >= 10:
            winner1 = True
        elif player2_length -2 >= 10:
            winner2 = True

        while winner1:
            # Mostrar game over y opciones
            winner_text = font_style.render("Player 1 Wins!", True, green)
            window.fill(black)
            restart_text = score_font.render("Press R to Restart or Q to Quit", True, white)
            window.blit(winner_text, (width / 2 - 100   , height / 2 - 50))
            window.blit(restart_text, (width / 2 - 150, height / 2))
            pygame.display.update()

            # Usar teclas en el Game Over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()
                    if event.key == pygame.K_q:
                        game_over = True
                        winner1 = False
        
        while winner2:
            # Mostrar game over y opciones
            winner_text = font_style.render("Player 2 Wins!", True, blue)
            window.fill(black)
            restart_text = score_font.render("Press R to Restart or Q to Quit", True, white)
            window.blit(winner_text, (width / 2 - 100, height / 2 - 50))
            window.blit(restart_text, (width / 2 - 150, height / 2))
            pygame.display.update()

            # Usar teclas en el Game Over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game()
                    if event.key == pygame.K_q:
                        game_over = True
                        winner2 = False
# --------------
        # Bindear teclas


 

        
        # Bindear teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player1_x_change != snake_block:
                    player1_x_change = -snake_block
                    player1_y_change = 0
                elif event.key == pygame.K_RIGHT and player1_x_change != -snake_block:
                    player1_x_change = snake_block
                    player1_y_change = 0
                elif event.key == pygame.K_UP and player1_y_change != snake_block:
                    player1_y_change = -snake_block
                    player1_x_change = 0
                elif event.key == pygame.K_DOWN and player1_y_change != -snake_block:
                    player1_y_change = snake_block
                    player1_x_change = 0
                elif event.key == pygame.K_a and player2_x_change != snake_block:
                    player2_x_change = -snake_block
                    player2_y_change = 0
                elif event.key == pygame.K_d and player2_x_change != -snake_block:
                    player2_x_change = snake_block
                    player2_y_change = 0
                elif event.key == pygame.K_w and player2_y_change != snake_block:
                    player2_y_change = -snake_block
                    player2_x_change = 0
                elif event.key == pygame.K_s and player2_y_change != -snake_block:
                    player2_y_change = snake_block
                    player2_x_change = 0

# --------------

        # Actualizar las posiciones de las serpientes
        player1_x += player1_x_change
        player1_y += player1_y_change
        player2_x += player2_x_change
        player2_y += player2_y_change

        # Colisiones
        if (
            player1_x >= width
            or player1_x < 0
            or player1_y >= height
            or player1_y < 0
            or (player1_x, player1_y) in player2_snake_list
            or (player1_x, player1_y) in player1_snake_list[2:]  # Check if player 1 collides with itself
        ):
            game_close = True
        if (
            player2_x >= width
            or player2_x < 0
            or player2_y >= height
            or player2_y < 0
            or (player2_x, player2_y) in player1_snake_list
            or (player2_x, player2_y) in player2_snake_list[2:]  # Check if player 2 collides with itself
        ):
            game_close = True

        # Actualizar las listas de posiciones de las serpientes
        player1_snake_list.append((player1_x, player1_y))
        player2_snake_list.append((player2_x, player2_y))
        if len(player1_snake_list) > player1_length:
            del player1_snake_list[0]
        if len(player2_snake_list) > player2_length:
            del player2_snake_list[0]

        # Ventana del juego
        window.fill(black)
        pygame.draw.rect(window, red, [fruit_x, fruit_y, snake_block, snake_block])
        draw_snake(player1_snake_list, green)
        draw_snake(player2_snake_list, blue)
        show_score(player1_length - 2, player2_length - 2)
        update_highscore("Player 1", player1_length - 2, player2_length -2)
        update_highscore("Player 2", player2_length - 2, player2_length -2)
        pygame.display.update()

        # Verificar si las serpientes comen la fruta
        if player1_x == fruit_x and player1_y == fruit_y:
            fruit_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            player1_length += 1
        if player2_x == fruit_x and player2_y == fruit_y:
            fruit_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            player2_length += 1

        # Velocidad del juego
        clock.tick(snake_speed)


    # Cerrar pygame
    pygame.quit()

# Iniciar el juego
game()