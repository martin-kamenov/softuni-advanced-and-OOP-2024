def even_odd(*data):
    command, numbers = data[-1], data[:-1]

    filter_func = {
        'even': lambda x: filter(lambda a: a % 2 == 0, x),
        'odd': lambda x: filter(lambda a: a % 2 != 0, x)
    }

    return list(filter_func[command](numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
