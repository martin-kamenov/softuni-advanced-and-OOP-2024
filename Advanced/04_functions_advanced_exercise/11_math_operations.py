def math_operations(*numbers, **operations):
    for index in range(len(numbers)):
        if index % 4 == 0:
            operations['a'] += numbers[index]
        elif index % 4 == 1:
            operations['s'] -= numbers[index]
        elif index % 4 == 2:
            if not numbers[index] == 0:
                operations['d'] /= numbers[index]
        elif index % 4 == 3:
            operations['m'] *= numbers[index]

    sorted_elements = dict(sorted(operations.items(), key=lambda x: (-x[1], x[0])))

    return '\n'.join(f'{key}: {value:.1f}' for key, value in sorted_elements.items())


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))