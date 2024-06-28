def valid_indexes(curr_row, curr_col):
    return 0 <= curr_row < size and 0 <= curr_col < size


size = int(input())
commands = input().split()

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

matrix = []
miner_pos = ()
collected_coal, total_coal = 0, 0

for row in range(size):
    matrix.append(input().split())

    if 's' in matrix[row]:
        index = matrix[row].index('s')
        miner_pos = (row, index)
        matrix[miner_pos[0]][miner_pos[1]] = '*'

    total_coal += matrix[row].count('c')

for command in commands:
    row, col = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not valid_indexes(row, col):
        continue

    miner_pos = (row, col)

    if matrix[row][col] == 'c':
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({row}, {col})")
            break

    elif matrix[row][col] == 'e':
        print(f"Game over! ({row}, {col})")
        raise SystemExit

    matrix[row][col] = '*'

else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
