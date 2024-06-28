def create_matrix_data():
    current_row = int(input())
    current_matrix = []

    for row in range(current_row):
        input_data = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
        current_matrix.append(input_data)

    return current_matrix


matrix = create_matrix_data()
print(matrix)
