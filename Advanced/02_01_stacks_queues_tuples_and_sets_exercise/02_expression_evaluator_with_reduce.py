from functools import reduce
from math import floor

symbols = input().split()
index = 0

functions = {
    "*": lambda idx: reduce(lambda a, b: a * b, map(int, symbols[:idx])),
    "/": lambda idx: reduce(lambda a, b: a / b, map(int, symbols[:idx])),
    "-": lambda idx: reduce(lambda a, b: a - b, map(int, symbols[:idx])),
    "+": lambda idx: reduce(lambda a, b: a + b, map(int, symbols[:idx]))
}

while len(symbols) > index:
    symbol = symbols[index]

    if symbol in "*/-+":
        symbols[0] = functions[symbol](index)
        [symbols.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(floor(int(symbols[0])))
