number = int(input())

matrix = [[int(el) for el in input().split()]for row in range(number)]
primary_diagonal = [matrix[row][row] for row in range(number)]
secondary_diagonal = [matrix[row][number - row - 1] for row in range(number)]
difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)


number = int(input())

matrix = [[int(el) for el in input().split()]for row in range(number)]

primary_sum, secondary_sum = 0, 0

for row in range(number):
    primary_sum += matrix[row][row]
    secondary_sum += matrix[row][number - row - 1]

result = abs(primary_sum - secondary_sum)

print(result)