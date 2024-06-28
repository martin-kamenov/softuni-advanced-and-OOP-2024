number = int(input())

matrix = [list(input()) for _ in range(number)]

searched_symbol = input()

for row in range(number):
    for col in range(len(matrix[row])):
        if searched_symbol == matrix[row][col]:
            coordinates = row, col

            print(coordinates)

            raise SystemExit

print(f'{searched_symbol} does not occur in the matrix')
