def find_start_position(rows_, cols_, matrix):
    for row in range(rows_):
        for col in range(cols_):
            if matrix[row][col] == 'B':
                return [row, col]

    return None


def delivery_is_late(*position):
    return 0 <= position[0] < rows and 0 <= position[1] < cols


rows, cols = [int(x) for x in input().split()]

movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

neighbourhood = []

is_late = False
is_delivered = False

for house in range(rows):
    neighbourhood.append(list(input()))

current_position = find_start_position(rows, cols, neighbourhood)
starting_position = current_position.copy()

while True:
    move = input()

    current_position[0] += movements[move][0]
    current_position[1] += movements[move][1]

    if not delivery_is_late(current_position[0], current_position[1]):
        is_late = True
        print('The delivery is late. Order is canceled.')
        break

    elif neighbourhood[current_position[0]][current_position[1]] == 'P':
        neighbourhood[current_position[0]][current_position[1]] = 'R'
        print('Pizza is collected. 10 minutes for delivery.')

    elif neighbourhood[current_position[0]][current_position[1]] == 'A':
        neighbourhood[current_position[0]][current_position[1]] = 'P'
        print('Pizza is delivered on time! Next order...')
        is_delivered = True
        break

    elif neighbourhood[current_position[0]][current_position[1]] == '*':
        current_position[0] -= movements[move][0]
        current_position[1] -= movements[move][1]
        continue

    else:
        neighbourhood[current_position[0]][current_position[1]] = '.'

if not is_late:
    neighbourhood[starting_position[0]][starting_position[1]] = 'B'
else:
    neighbourhood[starting_position[0]][starting_position[1]] = ' '

[print(''.join(row)) for row in neighbourhood]