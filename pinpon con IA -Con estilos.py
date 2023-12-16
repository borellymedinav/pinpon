import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH = 800
HEIGHT = 400

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Configuración de la pantalla
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Tamaño de la paleta
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

# Velocidad de movimiento de las paletas
PADDLE_SPEED = 20

# Creación de las paletas
paddle1 = pygame.Rect(50, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Velocidad de movimiento de la pelota
BALL_SPEED_X = 10
BALL_SPEED_Y = 10

# Creación de la pelota
ball = pygame.Rect(WIDTH / 2 - 10, HEIGHT / 2 - 10, 20, 20)

ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Puntuación
score_paddle1 = 0
score_paddle2 = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
clock = pygame.time.Clock()

while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de la paleta controlada por el jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
        paddle1.y += PADDLE_SPEED

    # Movimiento de la paleta controlada por la IA
    if paddle2.y + PADDLE_HEIGHT / 2 < ball.y:
        paddle2.y += PADDLE_SPEED
    if paddle2.y + PADDLE_HEIGHT / 2 > ball.y:
        paddle2.y -= PADDLE_SPEED

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisión de la pelota con las paletas
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Colisión de la pelota con las paredes superior e inferior
    if ball.y > HEIGHT - 20 or ball.y < 0:
        ball_speed_y *= -1

    # Si la pelota sale de la pantalla, se incrementa la puntuación del jugador correspondiente
    if ball.x > WIDTH:
        score_paddle1 += 1
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
        ball.x = WIDTH / 2 - 10
        ball.y = HEIGHT / 2 - 10
    elif ball.x < 0:
        score_paddle2 += 1
        ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
        ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))
        ball.x = WIDTH / 2 - 10
        ball.y = HEIGHT / 2 - 10

    # Dibujo en pantalla
    screen.fill(BLACK)

    # Dibujo de la paleta controlada por el jugador
    pygame.draw.rect(screen, WHITE, paddle1)

    # Dibujo de la paleta controlada por la IA
    pygame.draw.rect(screen, WHITE, paddle2)

    # Dibujo de la pelota
    pygame.draw.ellipse(screen, GREEN, ball)

    # Dibujo de la línea central
    pygame.draw.aaline(screen, WHITE, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

    # Mostrar puntuación en pantalla
    score_text = font.render(str(score_paddle1) + " - " + str(score_paddle2), True, WHITE)
    screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, 10))

    # Actualización de la pantalla
    pygame.display.flip()
    clock.tick(60)

# Finalización de Pygame
pygame.quit()
