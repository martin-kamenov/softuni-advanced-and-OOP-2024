def cookbook(*args):
    cooking_book = {}

    for data in args:
        recipe_name, cuisine, *ingredients = data

        if cuisine not in cooking_book:
            cooking_book[cuisine] = {}
        cooking_book[cuisine] = recipe_name
        cuisine[recipe_name] = ingredients

    return cooking_book


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
