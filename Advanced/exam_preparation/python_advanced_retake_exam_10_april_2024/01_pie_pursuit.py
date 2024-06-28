from collections import deque

contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant_ = contestants.popleft()
    pie_ = pies.pop()

    if contestant_ >= pie_:
        contestant_ -= pie_

        if contestant_ > 0:
            contestants.append(contestant_)

    elif contestant_ < pie_:
        pie_ -= contestant_

        if pie_ == 1 and len(pies) > 1:
            pies[-1] += pie_
        else:
            pies.append(pie_)

if contestants:
    print('We will have to wait for more pies to be baked!')
    print(f'Contestants left: {", ".join(str(contestant) for contestant in contestants)}')

if not contestants and not pies:
    print("We have a champion!")

if pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(pie) for pie in pies)}")