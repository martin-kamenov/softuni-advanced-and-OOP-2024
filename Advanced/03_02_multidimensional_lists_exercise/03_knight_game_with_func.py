def knights_movement(given_row, given_col):
    global current_attacks

    for direction in directions:
        move_row, move_col = given_row + direction[0], given_col + direction[1]

        if valid_indexes(move_row, move_col):
            if matrix[move_row][move_col] == 'K':
                current_attacks += 1


def find_max_attack(attack):
    global max_attacks, position_of_knight_with_most_attacks

    if attack > max_attacks:
        max_attacks = attack
        position_of_knight_with_most_attacks = (row, col)

    return max_attacks, position_of_knight_with_most_attacks


def valid_indexes(rows, cols):
    return 0 <= rows < size and 0 <= cols < size


size = int(input())
matrix = [list(input()) for _ in range(size)]

removed_knights = 0

directions = (
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2)
)

while True:
    position_of_knight_with_most_attacks = ()
    max_attacks = 0

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == 'K':
                current_attacks = 0
                knights_movement(row, col)

                max_attacks, position_of_knight_with_most_attacks = find_max_attack(current_attacks)

    if position_of_knight_with_most_attacks:
        curr_row, curr_col = position_of_knight_with_most_attacks

        matrix[curr_row][curr_col] = '0'
        removed_knights += 1

    else:
        break

print(removed_knights)
