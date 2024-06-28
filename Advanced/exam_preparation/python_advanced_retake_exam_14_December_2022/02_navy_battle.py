size = int(input())
row_submarine, col_submarine = None, None
battlefield = []
BATTLE_CRUISERS = 3
hit_mines = 0
destroyed_ships = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    battlefield.append(list(input()))

    if 'S' in battlefield[row]:
        row_submarine, col_submarine = row, battlefield[row].index('S')
        battlefield[row_submarine][col_submarine] = '-'

while destroyed_ships != 3 and hit_mines != 3:
    direction = input()

    row_submarine += directions[direction][0]
    col_submarine += directions[direction][1]

    if battlefield[row_submarine][col_submarine] == '*':
        hit_mines += 1

        if hit_mines == 3:
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{row_submarine}, {col_submarine}]!')

    elif battlefield[row_submarine][col_submarine] == 'C':
        destroyed_ships += 1

        if BATTLE_CRUISERS == destroyed_ships:
            print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')

    battlefield[row_submarine][col_submarine] = '-'

battlefield[row_submarine][col_submarine] = 'S'

[print(''.join(row)) for row in battlefield]
