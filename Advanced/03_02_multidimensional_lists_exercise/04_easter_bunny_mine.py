def valid_indexes(curr_rows, curr_cols):
    return 0 <= curr_rows < size and 0 <= curr_cols < size


size = int(input())
matrix = []

bunny_pos = ()
max_collected_eggs = -float('inf')
best_direction = None
bunny_path = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    row_data = input().split()
    matrix.append(row_data)

    if 'B' in matrix[row]:
        col_index = matrix[row].index('B')
        bunny_pos = (row, col_index)

for direction, coordinates in directions.items():
    moving_row, moving_col = bunny_pos[0] + coordinates[0], bunny_pos[1] + coordinates[1]

    collected_eggs = 0
    path = []

    while valid_indexes(moving_row, moving_col):

        if matrix[moving_row][moving_col] == 'X':
            break

        collected_eggs += int(matrix[moving_row][moving_col])
        path.append([moving_row, moving_col])

        moving_row += coordinates[0]
        moving_col += coordinates[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        bunny_path = path

print(best_direction)
[print(row) for row in bunny_path]
print(max_collected_eggs)
