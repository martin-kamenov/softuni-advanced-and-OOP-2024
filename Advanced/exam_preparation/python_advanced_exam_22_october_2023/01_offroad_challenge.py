from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque(int(x) for x in input().split())
needed_amount_of_fuel = deque(int(x) for x in input().split())

altitude = 0
reached_altitudes = []
top = len(initial_fuel)

while initial_fuel and consumption_index:
    fuel = initial_fuel.pop()
    index = consumption_index.popleft()
    amount_of_fuel = needed_amount_of_fuel.popleft()

    result = fuel - index

    if result >= amount_of_fuel:
        altitude += 1
        reached_altitudes.append(f'Altitude {altitude}')
        print(f'John has reached: Altitude {altitude}')

    else:
        initial_fuel.append(fuel)
        consumption_index.appendleft(index)
        needed_amount_of_fuel.appendleft(amount_of_fuel)
        print(f'John did not reach: Altitude {altitude + 1}')
        break

else:
    print(f'John has reached all the altitudes and managed to reach the top!')
    raise SystemExit

if top != altitude and reached_altitudes:
    print(f'John failed to reach the top.')
    print(f'Reached altitudes: {", ".join(reached_altitudes)}')
else:
    print('John failed to reach the top.')
    print("John didn't reach any altitude.")
