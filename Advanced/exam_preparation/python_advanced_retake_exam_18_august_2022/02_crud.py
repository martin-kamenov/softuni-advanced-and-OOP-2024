def create_value(matrix_, direction, value):
    curr_row, curr_col = start_position

    row_move = curr_row + directions[direction][0]
    col_move = curr_col + directions[direction][1]

    if matrix_[row_move][col_move] == '.':
        matrix_[row_move][col_move] = value
        position = row_move, col_move

        return position, matrix_

    return start_position, matrix_


def update_value(matrix_, direction, value):
    curr_row, curr_col = start_position

    row_move = curr_row + directions[direction][0]
    col_move = curr_col + directions[direction][1]

    if matrix_[row_move][col_move].isalnum():
        matrix_[row_move][col_move] = value
        position = row_move, col_move

        return position, matrix_

    return start_position, matrix_


def delete_value(matrix_, direction):
    curr_row, curr_col = start_position

    row_move = curr_row + directions[direction][0]
    col_move = curr_col + directions[direction][1]

    if matrix_[row_move][col_move].isalnum():
        matrix_[row_move][col_move] = '.'
        position = row_move, col_move

        return position, matrix_

    return start_position, matrix_


def read_value(matrix_, direction):
    curr_row, curr_col = start_position

    row_move = curr_row + directions[direction][0]
    col_move = curr_col + directions[direction][1]

    if matrix_[row_move][col_move].isalnum():
        element = matrix_[row_move][col_move]
        position = row_move, col_move
        print(element)

        return position, matrix_

    return start_position, matrix_


ROWS, COLS = 6, 6
matrix = [input().split() for _ in range(ROWS)]
start_position = eval(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:

    current_data = input().split(', ')

    if current_data[0] == 'Stop':
        break

    command, *directions_data = current_data

    if command == 'Create':
        start_position, matrix = create_value(matrix, *directions_data)
    elif command == 'Update':
        start_position, matrix = update_value(matrix, *directions_data)
    elif command == 'Delete':
        start_position, matrix = delete_value(matrix, *directions_data)
    elif command == 'Read':
        start_position, matrix = read_value(matrix, *directions_data)

[print(*row) for row in matrix]
