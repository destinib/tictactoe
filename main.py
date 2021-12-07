import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CR0SS_WIDTH = 25
SPACE = 55
player = 1

#rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66,66,66)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(color=BG_COLOR)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

def setup_board():
    #horizontal
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    #vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            if board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CR0SS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CR0SS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
       draw_asc_diagonal_line(player)
       return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
       draw_desc_diagonal_line(player)
       return True

    return False


def draw_vertical_win_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_win_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, posY), (WIDTH-15, posY), 15)

def draw_asc_diagonal_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,15),  (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(BG_COLOR)
    setup_board()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

setup_board()

# player = 1
game_over = False
# game_over = True

#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
           mouseX = event.pos[0] #x
           mouseY = event.pos[1] #y

           clicked_row = int(mouseY // 200)
           clicked_col = int(mouseX // 200)

           if available_square(clicked_row, clicked_col):
               if player == 1:
                   mark_square(clicked_row, clicked_col, 1)
                   if check_win(player):
                       game_over = True
                   player = 2
               elif player == 2:
                   mark_square(clicked_row, clicked_col, 2)
                   if check_win(player):
                       game_over = True
                   player = 1
               draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()


    pygame.display.update()




