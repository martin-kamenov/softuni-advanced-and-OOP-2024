matrix = []

rows = 3
columns = 2

for row_index in range(rows):
    matrix.append([])  # -> create list in matrix
    for column_index in range(columns):
        matrix[row_index].append(0)  # -> add value(element(in this case number)) to the current list

# matrix = [[0] * columns for _ in range(rows)]  # -> same as above, but it's not a good choice.
# It's a good choice only when we want to fill the list with the same values.
print(matrix)


# Matrix -> all nested lists are with the same length. If the length nested lists are different ->
# -> these are only nested lists, but not Matrix




