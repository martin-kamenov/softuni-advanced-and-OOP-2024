from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

crafted = []
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic_values:
    material = materials.pop() if magic_values[0] or not materials[-1] else 0
    magic_level = magic_values.popleft() if material or not magic_values[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {'Doll', 'Wooden train'}.issubset(crafted) or {'Teddy bear', 'Bicycle'}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(s) for s in materials[::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(s) for s in magic_values)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
