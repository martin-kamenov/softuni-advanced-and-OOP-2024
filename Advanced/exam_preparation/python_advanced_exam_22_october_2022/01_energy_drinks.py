from collections import deque

milligrams_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

MAX_CAFFEINE = 300
initial_caffeine = 0

while milligrams_caffeine and energy_drinks:
    caffeine = milligrams_caffeine.pop()
    drink = energy_drinks.popleft()

    current_caffeine = caffeine * drink

    if initial_caffeine + current_caffeine <= MAX_CAFFEINE:
        initial_caffeine += current_caffeine
    else:
        energy_drinks.append(drink)
        initial_caffeine -= 30

        if initial_caffeine < 0:
            initial_caffeine = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(str(s) for s in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {initial_caffeine} mg caffeine.')