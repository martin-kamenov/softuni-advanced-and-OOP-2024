def index_is_valid(row_, col_):
    return 0 <= row_ < rows and 0 <= col_ < cols


rows, cols = [int(x) for x in input().split(',')]
total_cheese = 0
mouse_pos = None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

cupboard = []

for row in range(rows):
    cupboard.append(list(input()))

    if 'M' in cupboard[row]:
        mouse_pos = (row, cupboard[row].index('M'))
        cupboard[row][mouse_pos[1]] = '*'

    total_cheese += cupboard[row].count('C')

collected_cheese = 0

while True:
    direction = input()

    if direction == 'danger':
        if total_cheese:
            print('Mouse will come back later!')
        break

    row_mouse, col_mouse = mouse_pos

    row_mouse += directions[direction][0]
    col_mouse += directions[direction][1]

    if not index_is_valid(row_mouse, col_mouse):
        print('No more cheese for tonight!')
        break

    elif cupboard[row_mouse][col_mouse] == 'C':
        cupboard[row_mouse][col_mouse] = '*'
        collected_cheese += 1

        if total_cheese == collected_cheese:
            mouse_pos = (row_mouse, col_mouse)
            print('Happy mouse! All the cheese is eaten, good night!')
            break

    elif cupboard[row_mouse][col_mouse] == 'T':
        mouse_pos = (row_mouse, col_mouse)
        print('Mouse is trapped!')
        break

    elif cupboard[row_mouse][col_mouse] == '@':
        row_mouse -= directions[direction][0]
        col_mouse -= directions[direction][1]
        continue

    mouse_pos = (row_mouse, col_mouse)

cupboard[mouse_pos[0]][mouse_pos[1]] = 'M'

[print(''.join(row)) for row in cupboard]
