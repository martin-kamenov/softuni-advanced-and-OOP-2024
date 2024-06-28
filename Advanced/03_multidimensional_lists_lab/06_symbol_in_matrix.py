def create_matrix_func():
    number_of_rows = int(input())
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix


def find_the_element(current_matrix, symbol):
    for row in range(len(current_matrix)):
        for column in range(len(current_matrix[0])):
            current_symbol = current_matrix[row][column]

            if current_symbol == symbol:
                return row, column


def printing_func(current_matrix, symbol):
    if current_matrix:
        print(current_matrix)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = create_matrix_func()
searched_symbol = input()
printing_func(find_the_element(matrix, searched_symbol), searched_symbol)
