from functools import reduce


def operate(operator, *numbers):
    operations = {
        '+': lambda x: reduce(lambda a, b: a + b, x),
        '-': lambda x: reduce(lambda a, b: a - b, x),
        '*': lambda x: reduce(lambda a, b: a * b, x),
        '/': lambda x: reduce(lambda a, b: a / b if b != 0 else None, x)
    }

    return operations[operator](numbers)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
