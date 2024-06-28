from collections import deque

packages_weight = [int(x) for x in input().split()]
couriers_capacities = deque(int(x) for x in input().split())
total_delivered_weight = 0

while packages_weight and couriers_capacities:
    package = packages_weight.pop()
    courier_capacity = couriers_capacities.popleft()

    if courier_capacity >= package:

        if courier_capacity > package:
            courier_capacity -= 2 * package

            if courier_capacity > 0:
                couriers_capacities.append(courier_capacity)

        total_delivered_weight += package

    else:
        package -= courier_capacity
        packages_weight.append(package)
        total_delivered_weight += courier_capacity

print(f"Total weight: {total_delivered_weight} kg")

if not packages_weight and not couriers_capacities:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

if packages_weight:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(p) for p in packages_weight)}")

if couriers_capacities:
    print(f"Couriers are still on duty: "
          f"{', '.join(str(c) for c in couriers_capacities)} but there are no more packages to deliver.")