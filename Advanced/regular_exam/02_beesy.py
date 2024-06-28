size = int(input())
bee_energy = 15
MIN_NECTAR = 30
MOVE = 1
hive_is_not_reached = True
collected_nectar = 0
times_restored_energy = 0

bee_position = None
field = []

# if index goes out of range, returns the opposite side
directions = {
    'up': lambda r, c: [(r - 1) % size, c],
    'down': lambda r, c: [(r + 1) % size, c],
    'left': lambda r, c: [r, (c - 1) % size],
    'right': lambda r, c: [r, (c + 1) % size]
}

for row in range(size):
    field.append(list(input()))

    if 'B' in field[row]:
        bee_position = [row, field[row].index('B')]
        field[row][bee_position[1]] = '-'

while bee_energy and hive_is_not_reached:

    direction = input()
    bee_position = directions[direction](*bee_position)

    row_bee, col_bee = bee_position
    element = field[row_bee][col_bee]

    bee_energy -= MOVE

    if element == 'H':
        hive_is_not_reached = False
        break

    elif bee_energy <= 0 and collected_nectar < MIN_NECTAR:
        break

    elif bee_energy <= 0 and collected_nectar >= MIN_NECTAR:
        if times_restored_energy == 0:
            bee_energy = collected_nectar - MIN_NECTAR
            collected_nectar = MIN_NECTAR

            times_restored_energy += 1

        else:
            break

    elif element.isdigit():
        collected_nectar += int(element)
        field[row_bee][col_bee] = '-'

field[bee_position[0]][bee_position[1]] = 'B'

if not hive_is_not_reached and collected_nectar >= MIN_NECTAR:
    print(f"Great job, Beesy! The hive is full. Energy left: {bee_energy}")

elif not hive_is_not_reached and collected_nectar < MIN_NECTAR:
    print("Beesy did not manage to collect enough nectar.")

else:
    print("This is the end! Beesy ran out of energy.")

[print(''.join(row)) for row in field]
