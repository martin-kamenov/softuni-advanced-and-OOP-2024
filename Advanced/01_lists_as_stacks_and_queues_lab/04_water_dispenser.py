from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    name = input()

    if name == 'Start':
        break

    queue.append(name)

while True:
    command = input()

    if command == 'End':
        break

    elif command.startswith('refill'):
        command = command.split()
        refill_amount = int(command[1])
        water_quantity += refill_amount

    else:
        person = queue.popleft()
        current_litters = int(command)

        if water_quantity - current_litters < 0:
            print(f'{person} must wait')
        else:
            water_quantity -= int(command)
            print(f'{person} got water')

print(f'{water_quantity} liters left')