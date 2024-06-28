from collections import deque

kids = deque(input().split())
num = int(input())

turns = 0

while len(kids) > 1:
    for index in range(num - 1):

        first_kid = kids.popleft()
        kids.append(first_kid)

    print(f'Removed {kids.popleft()}')

print(f'Last is {kids[0]}')
