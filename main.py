import pygame
import sys
import time
from solver import solve
from generator import generate_board
pygame.init()

WIDTH = 540
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KESAVA'S SUDOKU AI")

# COLORS
BG_COLOR = (30,30,30)
GRID_COLOR = (220,220,220)
BUTTON_COLOR = (70,70,70)
TEXT_COLOR = (255,255,255)
SELECT_COLOR = (0,255,0)

font = pygame.font.SysFont("Arial", 40)
button_font = pygame.font.SysFont("Arial", 30)
timer_font = pygame.font.SysFont("Arial", 28)
board = generate_board()

selected = None

button_rect = pygame.Rect(170, 560, 200, 50)

start_time = time.time()

gap = WIDTH // 9


def draw_all():

    screen.fill(BG_COLOR)

    # HIGHLIGHT SELECTED CELL
    if selected:

        row, col = selected

        pygame.draw.rect(
            screen,
            SELECT_COLOR,
            (col * gap, row * gap, gap, gap),
            4
        )

    # DRAW NUMBERS
    for row in range(9):
        for col in range(9):

            if board[row][col] != 0:

                text = font.render(
                    str(board[row][col]),
                    True,
                    TEXT_COLOR
                )

                screen.blit(
                    text,
                    (col * gap + 20, row * gap + 15)
                )

    # DRAW GRID
    for i in range(10):

        thickness = 4 if i % 3 == 0 else 1

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, i * gap),
            (WIDTH, i * gap),
            thickness
        )

        pygame.draw.line(
            screen,
            GRID_COLOR,
            (i * gap, 0),
            (i * gap, WIDTH),
            thickness
        )

    # DRAW BUTTON
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    button_text = button_font.render(
        "SOLVE",
        True,
        TEXT_COLOR
    )

    screen.blit(button_text, (225, 570))

    # TIMER
    elapsed_time = int(time.time() - start_time)

    timer_text = timer_font.render(
        f"Time: {elapsed_time}s",
        True,
        TEXT_COLOR
    )

    screen.blit(timer_text, (20, 620))


running = True

while running:

    draw_all()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            # SELECT CELL
            if y < WIDTH:

                selected = (y // gap, x // gap)

            # SOLVE BUTTON
            if button_rect.collidepoint(event.pos):

                solve(board, draw_all)

        # KEYBOARD INPUT
        if event.type == pygame.KEYDOWN and selected:

            row, col = selected

            if event.key == pygame.K_1:
                board[row][col] = 1

            if event.key == pygame.K_2:
                board[row][col] = 2

            if event.key == pygame.K_3:
                board[row][col] = 3

            if event.key == pygame.K_4:
                board[row][col] = 4

            if event.key == pygame.K_5:
                board[row][col] = 5

            if event.key == pygame.K_6:
                board[row][col] = 6

            if event.key == pygame.K_7:
                board[row][col] = 7

            if event.key == pygame.K_8:
                board[row][col] = 8

            if event.key == pygame.K_9:
                board[row][col] = 9

            if event.key == pygame.K_BACKSPACE:
                board[row][col] = 0

    pygame.display.update()

pygame.quit()
sys.exit()