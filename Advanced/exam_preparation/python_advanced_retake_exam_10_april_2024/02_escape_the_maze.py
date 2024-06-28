size = int(input())
traveller_hp = 100
maze = []
player_row, player_col = None, None

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

for row in range(size):
    maze.append(list(input()))

    if 'P' in maze[row]:
        player_row, player_col = row, maze[row].index('P')

while True:
    direction = input()

    if not (0 <= directions[direction][0] + player_row < size and 0 <= directions[direction][1] + player_col < size):
        continue

    maze[player_row][player_col] = '-'
    player_row += directions[direction][0]
    player_col += directions[direction][1]

    if maze[player_row][player_col] == 'X':
        print('Player escaped the maze. Danger passed!')
        maze[player_row][player_col] = 'P'
        break

    elif maze[player_row][player_col] == 'H':
        traveller_hp += 15

        if traveller_hp > 100:
            traveller_hp = 100

    elif maze[player_row][player_col] == 'M':
        traveller_hp -= 40

        if traveller_hp <= 0:
            traveller_hp = 0
            print('Player is dead. Maze over!')
            maze[player_row][player_col] = 'P'
            break

    maze[player_row][player_col] = 'P'

print(f"Player's health: {traveller_hp} units")
[print(''.join(row)) for row in maze]
