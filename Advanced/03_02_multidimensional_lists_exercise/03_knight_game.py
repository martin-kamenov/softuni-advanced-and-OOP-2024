size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = {
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
}

removed_knights = 0

while True:
    knight_with_most_attacks = []
    max_attacks = 0

    for row in range(size):
        for col in range(size):

            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    moving_row = row + position[0]
                    moving_col = col + position[1]

                    if 0 <= moving_row < size and 0 <= moving_col < size:
                        if matrix[moving_row][moving_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [row, col]

    if knight_with_most_attacks:
        current_row, current_col = knight_with_most_attacks
        matrix[current_row][current_col] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)