from __init__ import *


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
            if current_cells[y][x] == 1 and ((neighbors > 3) or (neighbors < 2)):
                new_cells[y][x] = 0
                g.numOfCells -= 1
            elif current_cells[y][x] == 0 and neighbors == 3:
                new_cells[y][x] = 1
                g.numOfCells += 1
    update_matrix(height, width, current_cells, new_cells)


def main():
    pygame.init()

    pygame.display.set_icon(g.logo)
    pygame.display.set_caption("Game Of Life by Giocrom")

    # pygame.font.init()

    # font_size = 30
    # margin = 10
    # banner = (2 * g.margin) + g.font_size
    #
    # default_font = pygame.font.SysFont("Pixelated", g.font_size)
    # logo = pygame.image.load("logo32x32.png")
    #
    # img_cell = pygame.image.load("cell36x36.png")
    # img_block = pygame.image.load("block36x36.png")
    # img_blinker = pygame.image.load("blinker36x36.png")
    # img_spaceships = pygame.image.load("spaceships36x36.png")
    # shapes = {0: img_cell, 1: img_block, 2: img_blinker, 3: img_spaceships}

    # screen_width = 600
    # screen_height = 600

    # cell_size = 6
    # 
    # cols = int(screen_width / cell_size)
    # rows = int((screen_height - banner) / cell_size)
    # 
    # current_cells = [[0 for i in range(cols)] for j in range(rows)]
    # new_cells = [[0 for i in range(cols)] for j in range(rows)]

    # handler = {'1': block, '2': blinker, '3': spaceship}

    # global g.numOfCells
    # numOfCells = initialize_matrix(rows, cols, current_cells)
    # print(numOfCells)
    
    update_matrix(g.rows, g.cols, g.new_cells, g.current_cells)
    screen = pygame.display.set_mode((g.screen_width, g.screen_height), RESIZABLE)

    screen.fill((0, 0, 0))
    display_counter = g.default_font.render("Alive cells: " + str(g.numOfCells), False, (255, 255, 255))
    screen.blit(display_counter, (50, g.screen_height - g.margin - g.font_size))
    board.draw_board(g.current_cells, g.rows, g.cols, g.cell_size, screen)

    num_pressed = 0
    paused = False
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                board.initialize_matrix(g.rows, g.cols, g.new_cells, 0)
                update_matrix(g.rows, g.cols, g.current_cells, g.new_cells)
                g.numOfCells = 0

            # num_pressed = handler.get(pygame.key.get_pressed(), None)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                num_pressed = 0
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                num_pressed = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                num_pressed = 2
            elif pygame.key.get_pressed()[pygame.K_3]:
                num_pressed = 3

            # if pygame.mouse.get_pressed(num_buttons=3) == (0, 1, 0):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                paused = not paused

            if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                # print(int(y / cell_size), int(x / cell_size))
                y_pos = int(y / g.cell_size)
                x_pos = int(x / g.cell_size)

                if y >= (g.screen_height - g.banner - g.cell_size):
                    y_pos = int((g.screen_height - g.banner) / g.cell_size) - 1
                if g.new_cells[y_pos][x_pos] == 0:
                    if num_pressed == 0:
                        g.new_cells[y_pos][x_pos] = 1
                        g.numOfCells += 1
                    elif num_pressed == 1:
                        my_shapes.block(x_pos, y_pos, g.new_cells, g.rows, g.cols)
                    elif num_pressed == 2:
                        my_shapes.blinker(x_pos, y_pos, g.new_cells, g.rows, g.cols)
                    elif num_pressed == 3:
                        my_shapes.spaceship(x_pos, y_pos, g.new_cells, g.rows, g.cols)

            if pygame.mouse.get_pressed(num_buttons=3) == (0, 0, 1):
                (x, y) = pygame.mouse.get_pos()
                # print(int(y / cell_size), int(x / cell_size))
                y_pos = int(y / g.cell_size)
                x_pos = int(x / g.cell_size)

                if y >= (g.screen_height - g.banner - g.cell_size):
                    y_pos = int((g.screen_height - g.banner) / g.cell_size) - 1
                if g.new_cells[y_pos][x_pos] == 1:
                    g.new_cells[y_pos][x_pos] = 0
                    g.numOfCells -= 1

        screen.fill((0, 0, 0))
        display_counter = g.default_font.render("Alive cells: " + str(g.numOfCells), False, (255, 255, 255))

        pygame.draw.line(screen, (255, 255, 255), (0, g.screen_height - (2 * g.margin) - g.font_size),
                         (g.screen_width, g.screen_height - (2 * g.margin) - g.font_size), 1)

        screen.blit(display_counter, (50, g.screen_height - (g.banner/2) - (g.font_size/2)))

        screen.blit(g.shapes.get(num_pressed, g.img_cell),
                    (g.screen_width - g.banner / 2 - 36, g.screen_height - g.margin - 36))

        if paused:
            update_matrix(g.rows, g.cols, g.current_cells, g.new_cells)
            delta_time = 0
        else:
            next_generation(g.rows, g.cols, g.current_cells, g.new_cells)
            delta_time = 1/20

        board.draw_board(g.current_cells, g.rows, g.cols, g.cell_size, screen)
        pygame.display.flip()

        sleep(delta_time)


if __name__ == "__main__":
    main()
