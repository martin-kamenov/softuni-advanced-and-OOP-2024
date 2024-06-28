def read_matrix_func():
    current_rows, current_columns = map(int, input().split(', '))
    current_matrix = []

    for row in range(current_rows):
        row_data = list(map(int, input().split()))
        current_matrix.append(row_data)

    return current_matrix


def sum_of_matrix_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    column = len(matrix[0])
    sum_of_columns = []

    for column_index in range(column):
        column_sum = 0
        for row_index in range(rows):
            column_sum += matrix[row_index][column_index]

        sum_of_columns.append(column_sum)

    return sum_of_columns


data = sum_of_matrix_columns()

for num in data:
    print(num)
