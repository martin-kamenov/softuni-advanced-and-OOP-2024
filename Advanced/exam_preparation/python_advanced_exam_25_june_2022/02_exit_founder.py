def players_moves(matrix_, move, player, winner, need_rest):
    rows, cols = move[0], move[1]

    if matrix_[rows][cols] == 'E':
        print(f'{player} found the Exit and wins the game!')
        raise SystemExit

    elif matrix_[rows][cols] == 'T':
        print(f'{player} is out of the game! The winner is {winner}.')
        raise SystemExit

    elif matrix_[rows][cols] == 'W':
        need_rest = True
        print(f'{player} hits a wall and needs to rest.')

        return need_rest
    return need_rest


first_player, second_player = input().split(', ')
ROWS, COLS = 6, 6
matrix = [input().split() for _ in range(ROWS)]

first_player_need_rest = False
second_player_need_rest = False

while True:

    first_player_move = eval(input())

    if not first_player_need_rest:
        first_player_need_rest = players_moves(matrix, first_player_move, first_player,
                                               second_player, first_player_need_rest)
    else:
        first_player_need_rest = False

    second_player_move = eval(input())
    if not second_player_need_rest:
        second_player_need_rest = players_moves(matrix, second_player_move, second_player,
                                                first_player, second_player_need_rest)
    else:
        second_player_need_rest = False
