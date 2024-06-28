from functools import reduce


def operate(operator, *numbers):
    def addition():
        result = reduce(lambda a, b: a + b, numbers)
        return result

    def subtract():
        result = reduce(lambda a, b: a - b, numbers)
        return result

    def division():
        result = reduce(lambda a, b: a / b if b != 0 else None, numbers)
        return result

    def multiply():
        result = reduce(lambda a, b: a * b, numbers)
        return result

    if operator == "+":
        return addition()
    elif operator == "-":
        return subtract()
    elif operator == "/":
        return division()
    elif operator == "*":
        return multiply()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))