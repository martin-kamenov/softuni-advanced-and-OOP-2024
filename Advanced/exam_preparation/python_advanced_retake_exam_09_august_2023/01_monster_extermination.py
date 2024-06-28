from collections import deque

monsters_armors = deque([int(x) for x in input().split(',')])
striking_impacts = [int(x) for x in input().split(',')]

killed_monsters = 0

while monsters_armors and striking_impacts:
    armor = monsters_armors.popleft()
    strike = striking_impacts.pop()

    if strike >= armor:
        killed_monsters += 1
        strike -= armor

        if striking_impacts:
            striking_impacts[-1] += strike

        else:
            if strike > 0:
                striking_impacts.append(strike)

    else:
        armor -= strike
        monsters_armors.append(armor)

if not monsters_armors:
    print('All monsters have been killed!')

if not striking_impacts:
    print('The soldier has been defeated.')

print(f'Total monsters killed: {killed_monsters}')