from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
}

while bees and nectar:
    bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < bee:
        bees.appendleft(bee)
    else:
        honey += abs(functions[symbols.popleft()](bee, curr_nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(s) for s in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(s) for s in nectar)}")
