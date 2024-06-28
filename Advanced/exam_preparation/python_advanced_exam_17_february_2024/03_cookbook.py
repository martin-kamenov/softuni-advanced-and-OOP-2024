def cookbook(*args):
    cooking_book = {}

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in cooking_book:
            cooking_book[cuisine] = []
        cooking_book[cuisine].append([recipe_name, ingredients])

    sorted_cookbook = sorted(cooking_book.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cuisine, recipies in sorted_cookbook:
        sorted_recipies = sorted(recipies, key=lambda x: x[0])
        result += f'{cuisine} cuisine contains {len(sorted_recipies)} recipes:\n'
        for recipie, ingredients in sorted_recipies:
            result += f'  * {recipie} -> Ingredients: {", ".join(ingredients)}\n'

    return result.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
