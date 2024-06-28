def create_matrix():
    numbers_of_rows, number_of_columns = [int(x) for x in input().split(", ")]
    current_matrix = []

    for row in range(numbers_of_rows):
        list_of_numbers = [int(x) for x in input().split(", ")]
        current_matrix.append(list_of_numbers)

    return current_matrix


def sum_matrix_numbers(current_matrix):
    matrix_sum = 0

    for row in range(len(current_matrix)):
        matrix_sum += sum(current_matrix[row])

    return matrix_sum


def print_func(current_matrix):
    print(sum_matrix_numbers(current_matrix))
    print(current_matrix)


matrix = create_matrix()
print_func(matrix)
