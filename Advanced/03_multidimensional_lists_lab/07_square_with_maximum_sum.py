def find_square_with_max_sum(matrix):
    max_sum = float('-inf')
    max_square = []

    for row in range(len(matrix) - 1):
        for column in range(len(matrix[row]) - 1):
            current_sum = (matrix[row][column] +
                           matrix[row][column + 1] +
                           matrix[row + 1][column] +
                           matrix[row + 1][column + 1])
            if current_sum > max_sum:
                max_sum = current_sum
                max_square = [[matrix[row][column], matrix[row][column + 1]],
                              [matrix[row + 1][column], matrix[row + 1][column + 1]]]

    return max_square, max_sum


rows_range, columns_range = [int(x) for x in input().split(', ')]
current_matrix = [[int(x) for x in input().split(', ')]for _ in range(rows_range)]

max_square_result, square_max_sum = find_square_with_max_sum(current_matrix)

for current_row in max_square_result:
    print(' '.join(map(str, current_row)))

print(square_max_sum)
