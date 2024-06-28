from collections import deque

tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:

    curr_tool = tools.popleft()
    curr_substance = substances.pop()

    result = curr_tool * curr_substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(curr_tool + 1)
        curr_substance -= 1
        if curr_substance <= 0:
            continue

        substances.append(curr_substance)

if challenges:
    print('Harry is lost in the temple. Oblivion awaits him.')
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f'Tools: {", ".join(str(t) for t in tools)}')

if substances:
    print(f'Substances: {", ".join(str(s) for s in substances)}')

if challenges:
    print(f'Challenges: {", ".join(str(c) for c in challenges)}')
