from Functions import board
import pygame

pygame.font.init()
font_size = 30
margin = 10
banner = (2 * margin) + font_size

default_font = pygame.font.SysFont("Pixelated", font_size)
logo = pygame.image.load("Docs/logo32x32.png")

img_cell = pygame.image.load("Docs/cell36x36.png")
img_block = pygame.image.load("Docs/block36x36.png")
img_blinker = pygame.image.load("Docs/blinker36x36.png")
img_spaceships = pygame.image.load("Docs/spaceships36x36.png")
shapes = {0: img_cell, 1: img_block, 2: img_blinker, 3: img_spaceships}

screen_width = 1200
screen_height = 600

cell_size = 7
grid_size = 2

cols = int(screen_width / cell_size)
rows = int((screen_height - banner) / cell_size)

current_cells = [[0 for i in range(cols)] for j in range(rows)]
new_cells = [[0 for i in range(cols)] for j in range(rows)]

numOfCells = board.initialize_matrix(rows, cols, current_cells)