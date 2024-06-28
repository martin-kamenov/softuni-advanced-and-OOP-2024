size = int(input())
plane_row, plane_col = None, None
ARMOR = 300
ENEMY_COUNT = 4
airspace = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    airspace.append(list(input()))

    if 'J' in airspace[row]:
        plane_row, plane_col = row, airspace[row].index('J')

while ARMOR and ENEMY_COUNT:
    direction = input()

    if not (0 <= directions[direction][0] + plane_row < size and 0 <= directions[direction][1] + plane_col < size):
        continue
    airspace[plane_row][plane_col] = '-'
    plane_row += directions[direction][0]
    plane_col += directions[direction][1]

    if airspace[plane_row][plane_col] == '-':
        continue

    elif airspace[plane_row][plane_col] == 'E':
        if ENEMY_COUNT == 1:
            ENEMY_COUNT -= 1
            airspace[plane_row][plane_col] = 'J'

            print('Mission accomplished, you neutralized the aerial threat!')
            break

        else:
            ARMOR -= 100
            ENEMY_COUNT -= 1

            if ARMOR == 0:
                airspace[plane_row][plane_col] = 'J'
                print(f'Mission failed, your jetfighter was shot down! Last coordinates [{plane_row}, {plane_col}]!')
                break

    elif airspace[plane_row][plane_col] == 'R':
        ARMOR = 300
        airspace[plane_row][plane_col] = 'J'

[print(''.join(row)) for row in airspace]
