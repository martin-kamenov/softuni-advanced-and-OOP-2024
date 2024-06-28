def indexes_are_valid(row_, col_):
    return 0 <= row_ < size and 0 <= col_ < size


size = int(input())
balance = 100
game_board = []
gambler_row, gambler_col = None, None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    game_board.append(list(input()))

    if 'G' in game_board[row]:
        gambler_row, gambler_col = row, game_board[row].index('G')
        game_board[gambler_row][gambler_col] = '-'

jackpot_is_won = False

while True:
    direction = input()

    if direction == 'end':
        game_board[gambler_row][gambler_col] = 'G'
        break

    gambler_row += directions[direction][0]
    gambler_col += directions[direction][1]

    if not indexes_are_valid(gambler_row, gambler_col):
        print('Game over! You lost everything!')
        raise SystemExit

    elif game_board[gambler_row][gambler_col] == '-':
        continue

    elif game_board[gambler_row][gambler_col] == 'W':
        balance += 100
        game_board[gambler_row][gambler_col] = '-'

    elif game_board[gambler_row][gambler_col] == 'P':
        balance -= 200
        game_board[gambler_row][gambler_col] = '-'

    elif game_board[gambler_row][gambler_col] == 'J':
        balance += 100000
        game_board[gambler_row][gambler_col] = 'G'
        jackpot_is_won = True
        break

    # game_board[gambler_row][gambler_col] = 'G'

    if balance <= 0:
        game_board[gambler_row][gambler_col] = 'G'
        print('Game over! You lost everything!')
        raise SystemExit

if jackpot_is_won:
    print(f'You win the Jackpot!\nEnd of the game. Total amount: {balance}$')
else:
    print(f'End of the game. Total amount: {balance}$')

[print(''.join(row)) for row in game_board]
