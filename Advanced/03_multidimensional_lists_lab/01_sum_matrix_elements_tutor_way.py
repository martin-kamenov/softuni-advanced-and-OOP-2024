def read_matrix_func():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()
matrix_element_sum = sum([sum(current_element) for current_element in matrix])

# for index in range(len(matrix)):
#     current_row = matrix[index]
#     matrix_element_sum += sum(current_row)

print(matrix_element_sum)
print(matrix)