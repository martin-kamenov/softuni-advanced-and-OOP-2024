numbers = tuple(map(float, input().split()))
numbers_dict = {}

for number in numbers:
    if number not in numbers_dict:
        numbers_dict[number] = 0
    numbers_dict[number] += 1

for key, value in numbers_dict.items():
    print(f'{key} - {value} times')