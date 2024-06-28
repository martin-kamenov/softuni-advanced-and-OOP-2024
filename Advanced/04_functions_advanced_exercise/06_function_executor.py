def func_executor(*numbers):
    # result = []
    #
    # for func, args in numbers:
    #     result.append(f'{func.__name__} - {func(*args)}')

    result = {f'{func.__name__} - {func(*args)}' for func, args in numbers}

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
