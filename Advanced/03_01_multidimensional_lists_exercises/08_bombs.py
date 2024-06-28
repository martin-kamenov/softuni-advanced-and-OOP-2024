size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs_coordinates = [[int(x) for x in line.split(',')] for line in input().split()]

directions = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (0, 0)
)

for row, col in bombs_coordinates:
    if matrix[row][col] <= 0:
        continue

    for direct_row, direct_col in directions:
        move_row, move_col = row + direct_row, col + direct_col

        if 0 <= move_row < size and 0 <= move_col < size:
            matrix[move_row][move_col] -= matrix[row][col] if matrix[move_row][move_col] > 0 else 0

alive_cells = [num for row in range(size) for num in matrix[row] if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]


