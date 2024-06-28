rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_element = matrix[row][col]
        next_element = matrix[row][col + 1]
        element_below = matrix[row + 1][col]
        diagonal_element = matrix[row + 1][col + 1]

        sum_matrix = sum((current_element, next_element, element_below, diagonal_element))

        if sum_matrix > max_sum:
            max_sum = sum_matrix
            sub_matrix = [[current_element, next_element], [element_below, diagonal_element]]

[print(*row) for row in sub_matrix]
print(max_sum)
