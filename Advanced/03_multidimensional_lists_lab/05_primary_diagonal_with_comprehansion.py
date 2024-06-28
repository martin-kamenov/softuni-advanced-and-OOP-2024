number = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(number)]
diagonal_sum = sum([matrix[row][row] for row in range(number)])

print(diagonal_sum)
