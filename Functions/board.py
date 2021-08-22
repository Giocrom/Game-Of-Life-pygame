from Functions import global_vars as g
import pygame
from random import randint


def initialize_matrix(rows, cols, matrix, mode=1):
    with open("Population.txt", "w") as matrixText:
        counter = 0
        for y in range(rows):
            for x in range(cols):
                if mode == 1:
                    value = randint(0, 1)
                elif mode == 0:
                    value = 0
                else:
                    return 0
                matrix[y][x] = value
                counter += value
                matrixText.write(str(matrix[y][x]) + " ")
                # print(str(matrix[y][x]), end=" ")
            matrixText.write("\n")
            # print("\n")
    return counter


def draw_board(current_cells, rows, cols, cell_size, screen):
    white = (255, 255, 255)
    for j in range(rows):
        for i in range(cols):
            x = 1 + (i * cell_size)
            y = 1 + (j * cell_size)
            if current_cells[j][i] == 1:
                pygame.draw.rect(screen, white, (x, y, cell_size - g.grid_size, cell_size - g.grid_size))
