def sorting_cheeses(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese, quantity in sorted_items:
        result.append(cheese)
        result.extend(sorted(quantity, reverse=True))

    return "\n".join(str(s) for s in result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
