def create_matrix_func():
    row_range = int(input())
    current_matrix = []

    for row in range(row_range):
        row_data = list(map(int, input().split()))
        current_matrix.append(row_data)

    return current_matrix


def sum_matrix_primary_diagonal(curr_matrix):
    diagonal_sum = 0

    for row in range(len(curr_matrix)):
        diagonal_number = curr_matrix[row][row]  # -> curr_matrix[row][row] returns the searched diagonal number from
        diagonal_sum += diagonal_number          # the indexes, e.g. 0,0; 1,1; 2,2 ->
        # that's how to extract the diagonal number.

    return diagonal_sum


def sum_matrix_secondary_diagonal(current_matrix):
    diagonal_sum = 0

    for index in range(len(current_matrix) - 1, -1, -1):
        diagonal_number = current_matrix[index][(len(current_matrix) - index - 1)]
        diagonal_sum += diagonal_number

    return diagonal_sum


matrix = create_matrix_func()

print(matrix)
print(sum_matrix_primary_diagonal(matrix))
print(sum_matrix_secondary_diagonal(matrix))

