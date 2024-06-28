rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_of_cols = []

for col in range(cols):
    cols_sum = 0

    for row in range(rows):
        cols_sum += matrix[row][col]

    sum_of_cols.append(cols_sum)

print(*sum_of_cols, sep='\n')
