def boarding_passengers(capacity, *boarding_data):
    boarded_groups = {}
    result = []
    total_passengers = sum(group[0] for group in boarding_data)

    for guests, group in boarding_data:
        if capacity == 0:
            break

        if guests > capacity:
            continue

        capacity -= guests

        if group not in boarded_groups:
            boarded_groups[group] = 0

        boarded_groups[group] += guests

    sorted_boarded_groups = sorted(boarded_groups.items(), key=lambda x: (-x[1], x[0]))

    boarded_passengers = sum(boarded_groups.values())
    result.append(f"Boarding details by benefit plan:")

    for plan, passengers in sorted_boarded_groups:
        result.append(f"## {plan}: {passengers} guests")

    if boarded_passengers == total_passengers:
        result.append("All passengers are successfully boarded!")
    elif capacity > 0:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")
    elif len(boarding_data) > len(boarded_groups):
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")

    return "\n".join(result)


print(boarding_passengers(
        150,
        (35, 'Diamond'),
        (55, 'Platinum'),
        (35, 'Gold'),
        (25, 'First Cruiser'))
)

print(boarding_passengers(
        100,
        (20, 'Diamond'),
        (15, 'Platinum'),
        (25, 'Gold'),
        (25, 'First Cruiser'),
        (15, 'Diamond'),
        (10, 'Gold'))
)

print(boarding_passengers(
        120,
        (30, 'Gold'),
        (20, 'Platinum'),
        (30, 'Diamond'),
        (10, 'First Cruiser'),
        (31, 'Platinum'),
        (20, 'Diamond'))
)