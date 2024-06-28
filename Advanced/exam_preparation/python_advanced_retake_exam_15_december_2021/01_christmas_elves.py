from collections import deque

elves_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]

toys = 0
COOKIE = 1
total_used_energy = 0
counter = 0

while elves_energy and materials_in_box:
    energy = elves_energy.popleft()
    materials = materials_in_box.pop()
    is_clumsy = False

    if energy < 5:
        materials_in_box.append(materials)

        continue
    counter += 1

    if counter % 5 == 0:
        if energy >= materials:
            energy -= materials
            total_used_energy += materials
            is_clumsy = True
        else:
            materials_in_box.append(materials)
            doubled_energy = energy * 2
            elves_energy.append(doubled_energy)

    elif counter % 3 == 0:
        upgraded_materials_energy = materials * 2

        if energy >= upgraded_materials_energy:
            toys += 2
            energy -= upgraded_materials_energy
            energy += COOKIE
            total_used_energy += upgraded_materials_energy
            elves_energy.append(energy)
        else:
            materials_in_box.append(materials)
            doubled_energy = energy * 2
            elves_energy.append(doubled_energy)

    elif energy >= materials:
        toys += 1
        energy -= materials
        energy += COOKIE
        total_used_energy += materials
        elves_energy.append(energy)

    else:
        materials_in_box.append(materials)
        doubled_energy = energy * 2
        elves_energy.append(doubled_energy)

    if is_clumsy and counter % 3 == 0:
        toys -= 2

print(f'Toys: {toys}')
print(f'Energy: {total_used_energy}')

if elves_energy:
    print(f'Elves left: {", ".join(str(e) for e in elves_energy)}')
if materials_in_box:
    print(f'Boxes left: {", ".join(str(m) for m in materials_in_box)}')
