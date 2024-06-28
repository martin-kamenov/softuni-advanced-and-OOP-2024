def naughty_or_nice_list(santa_kids_list, *args, **kwargs):
    nice_kids, naughty_kids = [], []
    result = []

    def place_kid():
        if len(kids) == 1:
            nice_kids.append(kids[0][1]) if naughty_or_nice == 'Nice' else naughty_kids.append(kids[0][1])
            santa_kids_list.remove(*kids)

    for curr_data in args:
        number, naughty_or_nice = curr_data.split('-')
        kids = [data for data in santa_kids_list if data[0] == int(number)]
        place_kid()

    for name, naughty_or_nice in kwargs.items():
        kids = [data for data in santa_kids_list if data[1] == name]
        place_kid()

    if nice_kids:
        result.append(f'Nice: {", ".join(kid for kid in nice_kids)}')
    if naughty_kids:
        result.append(f'Naughty: {", ".join(kid for kid in naughty_kids)}')
    if santa_kids_list:
        result.append(f'Not found: {", ".join(n[1] for n in santa_kids_list)}')

    return '\n'.join(result)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
