def move_func(direction, steps):
    row = my_position[0] + (directions[direction][0] * steps)
    col = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= row < SIZE and 0 <= col < SIZE):
        return my_position
    if field[row][col] == 'x':
        return my_position

    return [row, col]


def shoot_func(direction):
    row = my_position[0] + directions[direction][0]
    col = my_position[1] + directions[direction][1]

    while 0 <= row < SIZE and 0 <= col < SIZE:
        if field[row][col] == 'x':
            field[row][col] = '.'
            return [row, col]

        row += directions[direction][0]
        col += directions[direction][1]


SIZE = 5

field = []

targets = 0
targets_hit = 0
targets_hit_position = []

my_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for current_row in range(SIZE):
    field.append(input().split())

    if 'A' in field[current_row]:
        my_position = [current_row, field[current_row].index('A')]

    targets += field[current_row].count('x')

for _ in range(int(input())):
    command, *data = input().split()

    if command == 'move':
        moving_direction, current_steps = data[0], data[1]
        my_position = move_func(moving_direction, int(current_steps))
    elif command == 'shoot':
        moving_direction = data[0]
        targets_down_position = shoot_func(moving_direction)

        if targets_down_position:
            targets_hit_position.append(targets_down_position)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_position, sep='\n')


# def indexes_are_valid(row_, col_):
#     return 0 <= row_ < SIZE and 0 <= col_ < SIZE
#
#
# def move_through_field(direction, steps):
#     row_ = player_position[0] + (directions[direction][0] * steps)
#     col_ = player_position[1] + (directions[direction][1] * steps)
#
#     if not indexes_are_valid(row_, col_):
#         return player_position
#
#     if shooting_field[row_][col_] == 'x':
#         return player_position
#
#     return [row_, col_]
#
#
# def shoot_func(direction):
#     row_ = player_position[0] + directions[direction][0]
#     col_ = player_position[1] + directions[direction][1]
#
#     while indexes_are_valid(row_, col_):
#
#         if shooting_field[row_][col_] == 'x':
#             shooting_field[row_][col_] = '.'
#             return [row_, col_]
#
#         row_ += directions[direction][0]
#         col_ += directions[direction][1]
#
#
# SIZE = 5
# shooting_field = []
# player_position = []
# targets_count = 0
# shot_targets = []
# hit_targets = 0
#
# directions = {
#     'right': (0, 1),
#     'left': (0, -1),
#     'up': (-1, 0),
#     'down': (1, 0),
# }
#
# for row in range(SIZE):
#     shooting_field.append(input().split())
#
#     if 'A' in shooting_field[row]:
#         player_position = [row, shooting_field[row].index('A')]
#         shooting_field[row][player_position[1]] = '.'
#
#     targets_count += shooting_field[row].count('x')
#
# for _ in range(int(input())):
#     commands_data = input().split()
#
#     if commands_data[0].startswith('move'):
#         player_position = move_through_field(commands_data[1], int(commands_data[2]))
#
#     elif commands_data[0].startswith('shoot'):
#         target_down = shoot_func(commands_data[1])
#
#         if target_down:
#             shot_targets.append(target_down)
#             hit_targets += 1
#
#         if targets_count == hit_targets:
#             print(f"Training completed! All {targets_count} targets hit.")
#             break
#
# if hit_targets < targets_count:
#     print(f"Training not completed! {targets_count - hit_targets} targets left.")
#
#
# [print(row_) for row_ in shot_targets]
