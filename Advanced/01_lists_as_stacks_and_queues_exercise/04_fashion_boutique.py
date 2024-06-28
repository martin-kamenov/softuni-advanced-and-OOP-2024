clothes = [int(s) for s in input().split()]

rack_capacity = int(input())
racks = 1

current_rack_space = rack_capacity

while clothes:
    cloth = clothes.pop()

    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth
    else:
        racks += 1
        current_rack_space = rack_capacity - cloth

print(racks)
