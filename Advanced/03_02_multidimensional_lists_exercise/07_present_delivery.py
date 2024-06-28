def valid_indexes(curr_row, curr_col):
    return 0 <= curr_row < neighborhood_size and 0 <= curr_col < neighborhood_size


def santa_move(santa_row, santa_col):
    while valid_indexes(santa_row, santa_col):
        santa_row += directions[direction][0]
        santa_col += directions[direction][1]


presents = int(input())
neighborhood_size = int(input())

neighborhood = []
santa_pos = []
total_nice_kids = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for house in range(neighborhood_size):
    neighborhood.append(input().split())

    if 'S' in neighborhood[house]:
        santa_pos = [house, neighborhood[house].index('S')]
        neighborhood[house][santa_pos[1]] = '-'

    total_nice_kids += neighborhood[house].count('V')

direction = input()

while direction != 'Christmas morning' and presents:
    santa_move_row = santa_pos[0] + directions[direction][0]
    santa_move_col = santa_pos[1] + directions[direction][1]

    direction = input()