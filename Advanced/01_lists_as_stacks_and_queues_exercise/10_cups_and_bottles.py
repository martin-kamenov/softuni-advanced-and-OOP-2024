from collections import deque

cups_sequence = deque([int(x) for x in input().split()])
bottles_sequence = [int(x) for x in input().split()]

wasted_water = 0

while cups_sequence and bottles_sequence:
    cup = cups_sequence.popleft()
    bottle = bottles_sequence.pop()

    if bottle >= cup:
        wasted_water += bottle - cup

    else:
        cup -= bottle
        cups_sequence.appendleft(cup)

if not cups_sequence:
    print('Bottles:', *bottles_sequence)
else:
    print('Cups:', *cups_sequence)

print(f'Wasted litters of water: {wasted_water}')