ROWS, COLS = 6, 6
rover_position = None
field = []

deposits = {
    'W': ['Water deposit', 0],
    'M': ['Metal deposit', 0],
    'C': ['Concrete deposit', 0],
}

directions = {
    'up': lambda r, c: [(r - 1) % ROWS, c],
    'down': lambda r, c: [(r + 1) % ROWS, c],
    'left': lambda r, c: [r, (c - 1) % COLS],
    'right': lambda r, c: [r, (c + 1) % COLS],
}

for row in range(ROWS):
    field.append(input().split())

    if 'E' in field[row]:
        rover_position = row, field[row].index('E')

movements = input().split(', ')

for direction in movements:
    rover_position = directions[direction](*rover_position)
    element = field[rover_position[0]][rover_position[1]]

    if element in deposits:
        print(f'{deposits[element][0]} found at ({rover_position[0]}, {rover_position[1]})')

        deposits[element][1] += 1

    elif element == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        break

if all([deposits['W'][1], deposits['M'][1], deposits['C'][1]]):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
