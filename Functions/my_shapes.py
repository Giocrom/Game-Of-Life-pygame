from Functions import global_vars as g


def cell(x, y, matrix, y_max, x_max, orientation):
    if g.new_cells[y][x] == 0:
        g.new_cells[y][x] = 1
        g.numOfCells += 1


def block(x, y, matrix, y_max, x_max, orientation):
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
    g.numOfCells += shape_cells - (matrix[y][x] + matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x + 1])
    matrix[y][x] = 1
    matrix[y][x + 1] = 1
    matrix[y + 1][x] = 1
    matrix[y + 1][x + 1] = 1


def blinker(x, y, matrix, y_max, x_max, orientation):
    y_room = y_max - y
    x_room = x_max - x
    shape_cells = 3
    shape_size_y = 3
    shape_size_x = 1

    if orientation == 0b01 or orientation == 0b11:
        shape_size_y = 1
        shape_size_x = 3

    if y_room < shape_size_y:
        y_offset = shape_size_y - y_room
        y -= y_offset
    if x_room < shape_size_x:
        x_offset = shape_size_x - x_room
        x -= x_offset

    if orientation == 0b01 or orientation == 0b11:
        g.numOfCells += shape_cells - (matrix[y][x] + matrix[y][x + 1] + matrix[y][x + 2])
        matrix[y][x] = 1
        matrix[y][x + 1] = 1
        matrix[y][x + 2] = 1
    else:
        g.numOfCells += shape_cells - (matrix[y][x] + matrix[y + 1][x] + matrix[y + 2][x])
        matrix[y][x] = 1
        matrix[y + 1][x] = 1
        matrix[y + 2][x] = 1


def spaceship(x, y, matrix, y_max, x_max, orientation):
    y_room = y_max - y
    x_room = x_max - x
    shape_cells = 5
    shape_size_y = 3
    shape_size_x = 3
    if y_room < shape_size_y:
        y_offset = shape_size_y - y_room
        y -= y_offset
    if x_room < shape_size_x:
        x_offset = shape_size_x - x_room
        x -= x_offset
    g.numOfCells += shape_cells - (matrix[y][x] + matrix[y + 1][x + 1] + matrix[y + 1][x + 2] +
                                   matrix[y][x + 2] + matrix[y + 2][x + 1])
    matrix[y][x] = 1
    matrix[y + 1][x + 1] = 1
    matrix[y + 1][x + 2] = 1
    matrix[y][x + 2] = 1
    matrix[y + 2][x + 1] = 1
