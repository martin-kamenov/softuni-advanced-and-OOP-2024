def index_is_valid(indexes):
    return 0 <= int(indexes[0]) < size and 0 <= int(indexes[1]) < size


def add_number(info):
    row, col, number = info
    matrix[int(row)][int(col)] += int(number)


def subtract_number(info):
    row, col, number = info
    matrix[int(row)][int(col)] -= int(number)


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

while True:

    command_info = input()

    if command_info == "END":
        break

    command, *data = command_info.split()

    if not index_is_valid(data):
        print("Invalid coordinates")

    elif command == "Add":
        add_number(data)

    elif command == "Subtract":
        subtract_number(data)

[print(*row) for row in matrix]


# def valid_indexes(indexes):
#     row, col = indexes[0], indexes[1]
#
#     return 0 <= row < rows and 0 <= col < rows
#
#
# def add(indexes):
#     row, col, value = indexes
#     matrix[row][col] += value
#
#
# def subtract(indexes):
#     row, col, value = indexes
#     matrix[row][col] -= value
#
#
# rows = int(input())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# command = input().split()
#
# while command[0] != 'END':
#
#     action, *data = [x if x.isalpha() else int(x) for x in command]
#
#     if valid_indexes(data):
#         if action == 'Add':
#             add(data)
#         elif action == 'Subtract':
#             subtract(data)
#     else:
#         print('Invalid coordinates')
#
#     command = input().split()
#
# [print(*row) for row in matrix]



