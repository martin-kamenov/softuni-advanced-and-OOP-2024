from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])
matches = 0
worms_size = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm <= 0:
        holes.appendleft(hole)
    elif worm == hole:
        matches += 1
    else:
        worms.append(worm - 3)

if matches:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if not worms and matches == worms_size:
    print('Every worm found a suitable hole!')
elif not worms:
    print('Worms left: none')
else:
    print(f'Worms left: {", ".join(str(w) for w in worms)}')

if holes:
    print(f'Holes left: {", ".join(str(h) for h in holes)}')
else:
    print('Holes left: none')
