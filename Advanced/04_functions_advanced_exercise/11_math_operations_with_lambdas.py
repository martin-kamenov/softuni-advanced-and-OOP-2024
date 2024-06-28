def math_operations(*numbers, **data):
    operations = {
        'a': lambda x, y: x + y,
        's': lambda x, y: x - y,
        'd': lambda x, y: x / y if y != 0 else x,
        'm': lambda x, y: x * y,
    }

    keys = list(operations.keys())

    for index in range(len(numbers)):
        key = keys[index % 4]
        operation = operations[key]
        data[key] = operation(data[key], numbers[index])

    sorted_data = sorted(data.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f'{curr_key}: {curr_value:.1f}' for curr_key, curr_value in sorted_data)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
