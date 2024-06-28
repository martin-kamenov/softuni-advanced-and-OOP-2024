def grocery_store(**grocery_pairs):
    grocery_pairs = sorted(grocery_pairs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    # result = []
    #
    # for product, quantity in grocery_pairs:
    #     result.append(f'{product}: {quantity}')

    result = {f'{product}: {quantity}' for product, quantity in grocery_pairs}

    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
