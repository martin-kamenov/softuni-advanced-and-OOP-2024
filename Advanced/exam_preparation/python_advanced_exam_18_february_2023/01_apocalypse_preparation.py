from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

healing_items = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}

max_key_value = max(healing_items)
created_items = {}

while textile and medicaments:
    cloth = textile.popleft()
    medicament_ = medicaments.pop()
    result = cloth + medicament_

    if result in healing_items:
        if healing_items[result] not in created_items:
            created_items[healing_items[result]] = 0
        created_items[healing_items[result]] += 1

    elif result > max_key_value:
        if healing_items[max_key_value] not in created_items:
            created_items[healing_items[max_key_value]] = 0
        created_items[healing_items[max_key_value]] += 1

        difference = result - max_key_value

        if medicaments:
            medicaments[-1] += difference

    else:
        medicaments.append(medicament_ + 10)

if not medicaments and not textile:
    print('Textiles and medicaments are both empty.')
elif not textile:
    print('Textiles are empty.')
else:
    print('Medicaments are empty.')

if created_items:
    sorted_created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    [print(f'{item} - {amount}')for item, amount in sorted_created_items]

if medicaments:
    print(f'Medicaments left: {", ".join(reversed([str(s) for s in medicaments]))}')
if textile:
    print(f'Textiles left: {", ".join(str(t) for t in textile)}')
