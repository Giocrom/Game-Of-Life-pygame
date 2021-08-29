from __init__ import *


def count_neighbors(matrix, height, width, x, y):
    # print("pixel(" + str(y) + ";" + str(x) + ") is " + str(matrix[y][x]))

    if x == 0 and y == 0:
        # print("Case: Up-Left Angle")
        alive_neighbors = matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x]
        return alive_neighbors

    elif (x == width - 1) and y == 0:
        # print("Case: Up-Right Angle")
        alive_neighbors = matrix[y][x - 1] + matrix[y + 1][x] + matrix[y + 1][x - 1]
        return alive_neighbors

    elif x == 0 and (y == height - 1):
        # print("Case: Bottom-Left Angle")
        alive_neighbors = matrix[y-1][x+1] + matrix[y-1][x] + matrix[y][x+1]
        return alive_neighbors

    elif (x == width - 1) and (y == height - 1):
        # print("Case: Bottom-Right Angle")
        alive_neighbors = matrix[y][x - 1] + matrix[y - 1][x - 1] + matrix[y - 1][x]
        return alive_neighbors

    elif x != 0 and y == 0:
        # print("Case: Top-Line")
        alive_neighbors = (matrix[y][x - 1] + matrix[y + 1][x - 1] + matrix[y + 1][x] +
                           matrix[y + 1][x + 1] + matrix[y][x + 1])
        return alive_neighbors

    elif x == 0 and y != 0:
        # print("Case: Left-Line")
        alive_neighbors = (matrix[y - 1][x] + matrix[y - 1][x + 1] +
                           matrix[y][x + 1] + matrix[y + 1][x + 1] + matrix[y + 1][x])
        return alive_neighbors

    elif (x == width - 1) and y != 0:
        # print("Case: Right-Line")
        alive_neighbors = (matrix[y - 1][x] + matrix[y - 1][x - 1] +
                           matrix[y][x - 1] + matrix[y + 1][x - 1] + matrix[y + 1][x])
        return alive_neighbors

    elif (x != 0) and (y == height - 1):
        # print("Case: Bottom-Line")
        alive_neighbors = (matrix[y][x - 1] + matrix[y - 1][x - 1] +
                           matrix[y - 1][x] + matrix[y - 1][x + 1] + matrix[y][x + 1])
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

    update_matrix(g.rows, g.cols, g.new_cells, g.current_cells)
    screen = pygame.display.set_mode((g.screen_width, g.screen_height))

    screen.fill((0, 0, 0))
    display_counter = g.default_font.render("Alive cells: " + str(g.numOfCells), False, (255, 255, 255))
    screen.blit(display_counter, (50, g.screen_height - g.margin - g.font_size))
    board.draw_board(g.current_cells, g.rows, g.cols, g.cell_size, screen)

    num_pressed = 0
    orientation = 0b0000
    paused = False
    pygame.display.flip()


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            #     pygame.display.toggle_fullscreen()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                board.initialize_matrix(g.rows, g.cols, g.new_cells, 0)
                update_matrix(g.rows, g.cols, g.current_cells, g.new_cells)
                g.numOfCells = 0

            if event.type == pygame.KEYDOWN:
                num_pressed = g.handler.get(event.key, 0)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                paused = not paused

            if event.type == MOUSEWHEEL:
                orientation += (0b0001 * event.y)
                orientation = orientation & 0b0011

            if pygame.mouse.get_pressed(num_buttons=3) == (1, 0, 0):
                (x, y) = pygame.mouse.get_pos()
                # print(int(y / cell_size), int(x / cell_size))
                y_pos = int(y / g.cell_size)
                x_pos = int(x / g.cell_size)

                if y >= (g.screen_height - g.banner - g.cell_size):
                    y_pos = int((g.screen_height - g.banner) / g.cell_size) - 1

                draw = g.draw_handler.get(num_pressed, 0b0000)
                draw(x_pos, y_pos, g.new_cells, g.rows, g.cols, orientation)

            elif pygame.mouse.get_pressed(num_buttons=3) == (0, 0, 1):
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

        pygame.draw.line(screen, (255, 255, 255), (0, g.screen_height - g.banner),
                         (g.screen_width, g.screen_height - g.banner), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, g.screen_height), (g.screen_width, g.screen_height), 1)

        screen.blit(display_counter, (50, g.screen_height - g.banner + g.margin))

        orientation = orientation & 0b0011
        screen.blit(g.shapes.get((num_pressed + orientation), g.img_cell),
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
