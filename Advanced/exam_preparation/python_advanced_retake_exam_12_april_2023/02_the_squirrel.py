# 87% limit time

def indexes_are_valid(rows_, cols_):
    return 0 <= rows_ < size and 0 <= cols_ < size


def print_hazelnuts(nuts):
    print(f'Hazelnuts collected: {nuts}')


size = int(input())
movements = input().split(', ')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

field = []
squirrel_position = None
hazelnuts = 0

for row in range(size):
    field.append(list(input()))

    if 's' in field[row]:
        squirrel_position = (row, field[row].index('s'))


while hazelnuts != 3:

    row_squirrel, col_squirrel = squirrel_position

    for move in movements:
        row_on_move, col_on_move = directions[move]

        row_squirrel += row_on_move
        col_squirrel += col_on_move

        if not indexes_are_valid(row_squirrel, col_squirrel):
            print('The squirrel is out of the field.')
            print_hazelnuts(hazelnuts)
            raise SystemExit

        elif field[row_squirrel][col_squirrel] == 't':
            print('Unfortunately, the squirrel stepped on a trap...')
            print_hazelnuts(hazelnuts)
            raise SystemExit

        if field[row_squirrel][col_squirrel] == 'h':
            hazelnuts += 1
            field[row_squirrel][col_squirrel] = '*'
else:
    print('Good job! You have collected all hazelnuts!')

if hazelnuts < 3:
    print('There are more hazelnuts to collect.')

print_hazelnuts(hazelnuts)