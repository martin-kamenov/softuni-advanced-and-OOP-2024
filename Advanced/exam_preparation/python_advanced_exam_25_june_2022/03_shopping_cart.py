def shopping_cart(*products_data):
    max_soups, max_pizza, max_dessert = 3, 4, 2

    shop_cart = {'Soup': set(), 'Pizza': set(), 'Dessert': set()}
    result = []

    for lane in products_data:
        if lane == 'Stop':
            break

        meal, product = lane

        if len(shop_cart[meal]) == max_soups and meal == 'Soup':
            continue
        if len(shop_cart[meal]) == max_pizza and meal == 'Pizza':
            continue
        if len(shop_cart[meal]) == max_dessert and meal == 'Dessert':
            continue

        shop_cart[meal].add(product)

    for value in shop_cart.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_shop_cart = sorted(shop_cart.items(), key=lambda x: (-len(x[1]), x[0]))

    for curr_meal, products in sorted_shop_cart:
        sorted_products = sorted(products)
        result.append(f'{curr_meal}:')

        for curr_product in sorted_products:
            result.append(f' - {curr_product}')

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
