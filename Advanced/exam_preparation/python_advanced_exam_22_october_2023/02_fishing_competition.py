size = int(input())
QUOTA = 20
collected_fish = 0

player_position = []
fishing_area = []

movements = {
    'up': lambda r, c: [(r - 1) % size, c],
    'down': lambda r, c: [(r + 1) % size, c],
    'left': lambda r, c: [r, (c - 1) % size],
    'right': lambda r, c: [r, (c + 1) % size]
}

for row in range(size):
    fishing_area.append(list(input()))

    if 'S' in fishing_area[row]:
        player_position = [row, fishing_area[row].index('S')]
        fishing_area[row][player_position[1]] = '-'


while True:
    move = input()

    if move == 'collect the nets':
        break

    player_position = movements[move](*player_position)
    prow, pcol = player_position

    if fishing_area[prow][pcol].isdigit():
        collected_fish += int(fishing_area[prow][pcol])
        fishing_area[prow][pcol] = '-'

    elif fishing_area[prow][pcol] == 'W':
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
              f'Last coordinates of the ship: [{player_position[0]},{player_position[1]}]')
        collected_fish = 0
        raise SystemExit

fishing_area[player_position[0]][player_position[1]] = 'S'

if collected_fish >= QUOTA:
    print('Success! You managed to reach the quota!')
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {QUOTA - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f'Amount of fish caught: {collected_fish} tons.')

[print(''.join(row)) for row in fishing_area]