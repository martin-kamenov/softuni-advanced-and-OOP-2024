rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

print(sum([sum(el) for el in matrix]))
print(matrix)
