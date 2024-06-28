def find_player():
    for row in range(rows):
        if 'P' in matrix[row]:
            return row, matrix[row].index('P')


def find_bunnies_positions():
    bunnies_positions = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 'B':
                bunnies_positions.append((row, col))

    return bunnies_positions


def bunnies_movements(positions):
    for row, col in positions:
        for bunny_move in directions.values():
            new_row, new_col = row + bunny_move[0], col + bunny_move[1]

            if valid_indexes(new_row, new_col):
                matrix[new_row][new_col] = 'B'


def print_func(status='won'):
    [print(*row, sep='') for row in matrix]
    print(f'{status}: {player_row} {player_col}')

    raise SystemExit


def valid_indexes(curr_row, curr_col, player=False):
    global win

    if 0 <= curr_row < rows and 0 <= curr_col < cols:
        return True
    if player:
        win = True


def check_if_player_alive(row, col):
    if matrix[row][col] == 'B':
        print_func('dead')


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands = list(input())
win = False

directions = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0)
}

player_row, player_col = find_player()
matrix[player_row][player_col] = '.'

for command in commands:
    player_move_row, player_move_col = (player_row + directions[command][0],
                                        player_col + directions[command][1])
    if valid_indexes(player_move_row, player_move_col, player=True):
        player_row, player_col = player_move_row, player_move_col

    bunnies_movements(find_bunnies_positions())

    if win:
        print_func()

    check_if_player_alive(player_row, player_col)