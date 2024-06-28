SIZE = 8

board = []
positions = [[], []]


def save_pawn_position(element, save_to_index, row_):
    if element in board[row_]:
        positions[save_to_index].append(row_)
        positions[save_to_index].append(board[row_].index(element))


for row in range(SIZE):
    board.append(input().split())

    save_pawn_position('w', 0, row)
    save_pawn_position('b', 1, row)

if abs(positions[0][1] - positions[1][1]) != 1:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f'Game over! Black pawn is promoted to a queen at {chr( 97 + positions[1][1])}1.')
    else:
        print(f'Game over! White pawn is promoted to a queen at {chr( 97 + positions[0][1])}8.')
else:
    middle = (positions[0][0] + positions[1][0]) // 2

    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f'Game over! Black win, capture on {chr( 97 + positions[0][1])}{SIZE - middle}.')
    else:
        print(f'Game over! White win, capture on {chr( 97 + positions[1][1])}{SIZE - middle}.')