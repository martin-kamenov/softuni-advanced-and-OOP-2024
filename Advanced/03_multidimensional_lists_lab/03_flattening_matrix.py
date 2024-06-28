def create_matrix():
    current_rows = int(input())
    current_matrix = []

    for row in range(current_rows):
        numbers_data = list(map(int, input().split(', ')))
        current_matrix.append(numbers_data)

    return current_matrix


matrix = create_matrix()

flattened_matrix = [el for row in matrix for el in row]
print(flattened_matrix)
