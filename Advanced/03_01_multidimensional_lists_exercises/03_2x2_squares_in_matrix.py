rows, columns = [int(x) for x in input().split()]
matrix = [[el for el in input().split()]for row in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        element = matrix[row][column]

        if (element == matrix[row + 1][column] and
                element == matrix[row][column + 1] and
                element == matrix[row + 1][column + 1]):
            equal_blocks += 1

print(equal_blocks)


# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# squares_count = 0
#
# for row in range(rows - 1):
#     for col in range(cols - 1):
#         if (matrix[row][col] ==
#                 matrix[row][col+1] ==
#                 matrix[row+1][col] ==
#                 matrix[row+1][col+1]):
#             squares_count += 1
#
# print(squares_count)
