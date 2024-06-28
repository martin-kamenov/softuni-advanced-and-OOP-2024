number = int(input())

matrix = [[int(x) for x in input().split(', ')]for row in range(number)]
primary_diagonal = [matrix[row][row] for row in range(number)]
secondary_diagonal = [matrix[row][number - row - 1] for row in range(number)]

print(f'Primary diagonal: {", ".join(str(s) for s in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(s) for s in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')