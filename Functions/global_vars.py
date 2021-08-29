from Functions import board
from Functions import my_shapes
import pygame

pygame.font.init()
font_size = 30
margin = 10
banner = (2 * margin) + font_size

default_font = pygame.font.SysFont("Pixelated", font_size)
logo = pygame.image.load("Docs/logo32x32.png")

img_cell = pygame.image.load("Docs/cell36x36.png")
img_block = pygame.image.load("Docs/block36x36.png")

img_blinker_v = pygame.image.load("Docs/blinker36x36.png")
img_blinker_h = pygame.image.load("Docs/blinker_horizontal36x36.png")

img_spaceships_bottomright = pygame.image.load("Docs/spaceships_bottomright36x36.png")
img_spaceships_upright = pygame.image.load("Docs/spaceships_upright36x36.png")
img_spaceships_upleft = pygame.image.load("Docs/spaceships_upleft36x36.png")
img_spaceships_bottomleft = pygame.image.load("Docs/spaceships_bottomleft36x36.png")

shapes = {0b0000: img_cell,

          0b0100: img_block,
          0b0101: img_block,
          0b0110: img_block,
          0b0111: img_block,

          0b1000: img_blinker_v,
          0b1001: img_blinker_h,
          0b1010: img_blinker_v,
          0b1011: img_blinker_h,

          0b1100: img_spaceships_bottomright,
          0b1101: img_spaceships_upright,
          0b1110: img_spaceships_upleft,
          0b1111: img_spaceships_bottomleft
          }

handler = {pygame.K_0: 0b0000, pygame.K_1: 0b0100, pygame.K_2: 0b1000, pygame.K_3: 0b1100}
draw_handler = {0b0000: my_shapes.cell, 0b0100: my_shapes.block, 0b1000: my_shapes.blinker, 0b1100: my_shapes.spaceship}

screen_width = 1200
screen_height = 600

cell_size = 7
grid_size = 2

cols = int(screen_width / cell_size)
rows = int((screen_height - banner) / cell_size)

current_cells = [[0 for i in range(cols)] for j in range(rows)]
new_cells = [[0 for i in range(cols)] for j in range(rows)]

numOfCells = board.initialize_matrix(rows, cols, current_cells)
