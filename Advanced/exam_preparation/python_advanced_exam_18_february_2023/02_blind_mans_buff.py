rows, cols = [int(x) for x in input().split()]
OPPONENTS = 3

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

touched_players = 0
movements = 0
player_row, player_col = None, None
playground = []

for row in range(rows):
    playground.append(input().split())

    if 'B' in playground[row]:
        player_row, player_col = row, playground[row].index('B')
        playground[row][player_col] = '-'

while True:
    direction = input()

    if direction == 'Finish':
        break

    if touched_players == OPPONENTS:
        break

    possible_row_move = player_row + directions[direction][0]
    possible_col_move = player_col + directions[direction][1]

    if not (0 <= possible_row_move < rows and 0 <= possible_col_move < cols):
        possible_row_move, possible_col_move = None, None
        continue

    if playground[possible_row_move][possible_col_move] == 'O':
        possible_row_move, possible_col_move = None, None
        continue

    elif playground[possible_row_move][possible_col_move] == '-':
        player_row += directions[direction][0]
        player_col += directions[direction][1]
        movements += 1

    elif playground[possible_row_move][possible_col_move] == 'P':
        player_row += directions[direction][0]
        player_col += directions[direction][1]
        playground[player_row][player_col] = '-'
        touched_players += 1
        movements += 1

print(f"""
Game over!
Touched opponents: {touched_players} Moves made: {movements}
""")
