from collections import deque
from math import floor

symbols = deque(input())
index = 0

while len(symbols) > 1:
    symbol = symbols[index]

    if symbol == '*':
        for _ in range(index - 1):
            symbols.appendleft(int(symbols.popleft()) * int(symbols.popleft()))
    elif symbol == '/':
        for _ in range(index - 1):
            symbols.appendleft(int(symbols.popleft()) / int(symbols.popleft()))
    elif symbol == '-':
        for _ in range(index - 1):
            symbols.appendleft(int(symbols.popleft()) - int(symbols.popleft()))
    elif symbol == '+':
        for _ in range(index - 1):
            symbols.appendleft(int(symbols.popleft()) + int(symbols.popleft()))

    if symbol in "*/-+":
        del symbols[1]
        index = 1

    index += 1

print(floor(int(symbols[0])))
