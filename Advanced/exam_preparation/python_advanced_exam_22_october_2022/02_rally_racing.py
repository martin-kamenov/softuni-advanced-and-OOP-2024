size = int(input())
racing_number = input()
race_route = [input().split() for _ in range(size)]

row_car, col_car = 0, 0
passed_kilometers = 0
KILOMETERS_PER_MOVE = 10
TUNEL_KM = 30
is_found = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    direction = input()

    if direction == 'End':
        print(f'Racing car {racing_number} DNF.')
        break

    curr_row, curr_col = row_car, col_car

    curr_row += directions[direction][0]
    curr_col += directions[direction][1]

    if race_route[curr_row][curr_col] == 'F':
        passed_kilometers += KILOMETERS_PER_MOVE
        row_car, col_car = curr_row, curr_col
        print(f'Racing car {racing_number} finished the stage!')
        break

    elif race_route[curr_row][curr_col] == '.':
        row_car, col_car = curr_row, curr_col
        passed_kilometers += KILOMETERS_PER_MOVE

    elif race_route[curr_row][curr_col] == 'T':
        race_route[curr_row][curr_col] = '.'
        passed_kilometers += TUNEL_KM

        for row in range(size):
            for col in range(size):
                if race_route[row][col] == 'T':
                    race_route[row][col] = '.'
                    is_found = True
                    row_car, col_car = row, col
                    break

            if is_found:
                break

race_route[row_car][col_car] = 'C'

print(f'Distance covered {passed_kilometers} km.')
[print(''.join(row)) for row in race_route]
