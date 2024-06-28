def even_odd_filter(**data):
    if 'odd' in data:
        data['odd'] = [num for num in data['odd'] if num % 2 != 0]

    if 'even' in data:
        data['even'] = [num for num in data['even'] if num % 2 == 0]

    return dict(sorted(data.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
