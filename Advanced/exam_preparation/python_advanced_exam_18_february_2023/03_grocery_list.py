def shop_from_grocery_list(budget, grocery_list, *products):
    bought_products = 0
    purchased_products = set()

    for product, price in products:
        if grocery_list:
            if product in grocery_list:

                if budget < price:
                    break

                if product in purchased_products:
                    continue

                elif budget >= price:
                    budget -= price
                    bought_products += 1
                    purchased_products.add(product)

            elif product not in grocery_list:
                continue

    not_bought_products = purchased_products.symmetric_difference(grocery_list)

    if purchased_products.issuperset(grocery_list):
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'

    return (f'You did not buy all the products. '
            f'Missing products: {", ".join(not_bought_products)}.')


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
