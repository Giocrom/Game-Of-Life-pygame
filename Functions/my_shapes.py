from Functions import global_vars as g


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
    g.numOfCells += shape_cells - (matrix[y][x] + matrix[y][x + 1] + matrix[y + 1][x] + matrix[y + 1][x + 1])
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
    g.numOfCells += shape_cells - (matrix[y][x] + matrix[y + 1][x] + matrix[y + 2][x])
    matrix[y][x] = 1
    matrix[y+1][x] = 1
    matrix[y+2][x] = 1


def spaceship(x, y, matrix, y_max, x_max):
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