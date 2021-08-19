from time import sleep
import pygame
# import pymunk
from random import randint


numOfCells = 0


def block(x, y, matrix, y_max, x_max):
    y_room = y_max - y
    x_room = x_max - x
    shape_cells = 4
    shape_size = 2
    if y_room < shape_size:
        y_offset = shape_size - y_room
        y -= y_offset
    if x_room < shape_size:
        x_offset = shape_size - x_room
        x -= x_offset
    global numOfCells
    numOfCells += shape_cells - (matrix[y][x] + matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x + 1])
    matrix[y][x] = 1
    matrix[y][x + 1] = 1
    matrix[y + 1][x] = 1
    matrix[y + 1][x + 1] = 1


def blinker(x, y, matrix, y_max, x_max):
    y_room = y_max - y
    x_room = x_max - x
    shape_cells = 3
    shape_size_y = 3
    shape_size_x = 1
    if y_room < shape_size_y:
        y_offset = shape_size_y - y_room
        y -= y_offset
    if x_room < shape_size_x:
        x_offset = shape_size_x - x_room
        x -= x_offset
    global numOfCells
    numOfCells += shape_cells - (matrix[y][x] + matrix[y + 1][x] + matrix[y + 2][x])
    matrix[y][x] = 1
    matrix[y+1][x] = 1
    matrix[y+2][x] = 1


def spaceship(x, y, matrix):
    matrix[y][x] = 1
    matrix[y + 1][x + 1] = 1
    matrix[y + 2][x + 1] = 1
    matrix[y + 2][x] = 1
    matrix[y + 2][x - 1] = 1


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
    grid_size = 1
    for j in range(rows):
        for i in range(cols):
            x = 1 + (i * cell_size)
            y = 1 + (j * cell_size)
            if current_cells[j][i] == 1:
                pygame.draw.rect(screen, white, (x, y, cell_size - grid_size, cell_size - grid_size))


def count_neighbors(matrix, height, width, x, y):
    # print("pixel(" + str(y) + ";" + str(x) + ") is " + str(matrix[y][x]))

    if x == 0 and y == 0:
        # print("Case: Up-Left Angle")
        alive_neighbors = matrix[y][x+1] + matrix[y+1][x] + matrix[y+1][x]
        return alive_neighbors

    elif (x == width - 1) and y == 0:
        # print("Case: Up-Right Angle")
        alive_neighbors = matrix[y][x-1] + matrix[y+1][x] + matrix[y+1][x-1]
        return alive_neighbors

    elif x == 0 and (y == height - 1):
        # print("Case: Bottom-Left Angle")
        alive_neighbors = matrix[y-1][x+1] + matrix[y-1][x] + matrix[y][x+1]
        return alive_neighbors

    elif (x == width - 1) and (y == height - 1):
        # print("Case: Bottom-Right Angle")
        alive_neighbors = matrix[y][x-1] + matrix[y-1][x-1] + matrix[y-1][x]
        return alive_neighbors

    elif x != 0 and y == 0:
        # print("Case: Top-Line")
        alive_neighbors = matrix[y][x-1] + matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1] + matrix[y][x+1]
        return alive_neighbors

    elif x == 0 and y != 0:
        # print("Case: Left-Line")
        alive_neighbors = matrix[y-1][x] + matrix[y-1][x+1] + matrix[y][x+1] + matrix[y+1][x+1] + matrix[y+1][x]
        return alive_neighbors

    elif (x == width - 1) and y != 0:
        # print("Case: Right-Line")
        alive_neighbors = matrix[y-1][x] + matrix[y-1][x-1] + matrix[y][x-1] + matrix[y+1][x-1] + matrix[y+1][x]
        return alive_neighbors

    elif (x != 0) and (y == height - 1):
        # print("Case: Bottom-Line")
        alive_neighbors = matrix[y][x-1] + matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] + matrix[y][x+1]
        return alive_neighbors

    else:
        # print("Case: In Grid")
        alive_neighbors = (matrix[y-1][x-1] + matrix[y-1][x] + matrix[y-1][x+1] +
                           matrix[y][x+1] + matrix[y][x-1] +
                           matrix[y+1][x-1] + matrix[y+1][x] + matrix[y+1][x+1])
        return alive_neighbors


def update_matrix(height, width, current_cells, new_cells):
    for y in range(height):
        for x in range(width):
            if new_cells[y][x] == 0:
                current_cells[y][x] = 0
            else:
                current_cells[y][x] = 1


def next_generation(height, width, current_cells, new_cells):
    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(current_cells, height, width, x, y)
            global numOfCells

            if current_cells[y][x] == 1 and ((neighbors > 3) or (neighbors < 2)):
                new_cells[y][x] = 0
                numOfCells -= 1
            elif current_cells[y][x] == 0 and neighbors == 3:
                new_cells[y][x] = 1
                numOfCells += 1
    update_matrix(height, width, current_cells, new_cells)


def main():
    pygame.init()
    pygame.font.init()

    font_size = 30
    margin = 10
    banner = (2 * margin) + font_size

    default_font = pygame.font.SysFont("Pixelated", font_size)
    logo = pygame.image.load("logo32x32.png")

    img_cell = pygame.image.load("cell36x36.png")
    img_block = pygame.image.load("block36x36.png")
    img_blinker = pygame.image.load("blinker36x36.png")
    shapes = {0: img_cell, 1: img_block, 2: img_blinker}

    pygame.display.set_icon(logo)
    pygame.display.set_caption("Game Of Life by Giocrom")

    screen_width = 600
    screen_height = 600

    cell_size = 6

    cols = int(screen_width / cell_size)
    rows = int((screen_height - banner) / cell_size)

    current_cells = [[0 for i in range(cols)] for j in range(rows)]
    new_cells = [[0 for i in range(cols)] for j in range(rows)]

    # handler = {'1': block, '2': blinker, '3': spaceship}

    global numOfCells
    numOfCells = initialize_matrix(rows, cols, current_cells)
    # print(numOfCells)
    update_matrix(rows, cols, new_cells, current_cells)
    screen = pygame.display.set_mode((screen_width, screen_height))

    screen.fill((0, 0, 0))
    display_counter = default_font.render("Alive cells: " + str(numOfCells), False, (255, 255, 255))
    screen.blit(display_counter, (50, screen_height - margin - font_size))
    draw_board(current_cells, rows, cols, cell_size, screen)

    num_pressed = 0
    paused = False
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if pygame.key.get_pressed()[pygame.K_f]:
            #     pygame.display.toggle_fullscreen()

            if pygame.key.get_pressed()[pygame.K_d]:
                initialize_matrix(rows, cols, new_cells, 0)
                update_matrix(rows, cols, current_cells, new_cells)
                numOfCells = 0

            # num_pressed = handler.get(pygame.key.get_pressed(), None)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                num_pressed = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                num_pressed = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                num_pressed = 2
            # if pygame.key.get_pressed()[pygame.K_3]:
            #     num_pressed = 3

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            # if pygame.mouse.get_pressed(num_buttons=3) == (0, 1, 0):
                paused = not paused

            if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                # print(int(y / cell_size), int(x / cell_size))
                y_pos = int(y / cell_size)
                x_pos = int(x / cell_size)

                if y >= (screen_height - banner - cell_size):
                    y_pos = int((screen_height - banner) / cell_size) - 1
                if new_cells[y_pos][x_pos] == 0:
                    if num_pressed == 0:
                        new_cells[y_pos][x_pos] = 1
                        numOfCells += 1
                    elif num_pressed == 1:
                        block(x_pos, y_pos, new_cells, rows, cols)
                    elif num_pressed == 2:
                        blinker(x_pos, y_pos, new_cells, rows, cols)

            if pygame.mouse.get_pressed(num_buttons=3) == (0, 0, 1):
                (x, y) = pygame.mouse.get_pos()
                # print(int(y / cell_size), int(x / cell_size))
                y_pos = int(y / cell_size)
                x_pos = int(x / cell_size)

                if y >= (screen_height - banner - cell_size):
                    y_pos = int((screen_height - banner) / cell_size) - 1
                if new_cells[y_pos][x_pos] == 1:
                    new_cells[y_pos][x_pos] = 0
                    numOfCells -= 1

        screen.fill((0, 0, 0))

        display_counter = default_font.render("Alive cells: " + str(numOfCells), False, (255, 255, 255))
        pygame.draw.line(screen, (255, 255, 255), (0, screen_height - (2 * margin) - font_size),
                         (screen_width, screen_height - (2 * margin) - font_size), 1)
        screen.blit(display_counter, (50, screen_height - (banner/2) - (font_size/2)))
        screen.blit(shapes.get(num_pressed, img_cell), (screen_width - 50, screen_height - margin - 36))

        if paused:
            update_matrix(rows, cols, current_cells, new_cells)
            delta_time = 0
        else:
            next_generation(rows, cols, current_cells, new_cells)
            delta_time = 1/20

        draw_board(current_cells, rows, cols, cell_size, screen)
        pygame.display.flip()

        sleep(delta_time)


if __name__ == "__main__":
    main()
