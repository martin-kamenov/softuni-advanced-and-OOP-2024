def even_odd(*numbers):
    command = numbers[-1]

    if command == "odd":
        return [x for x in numbers[:-1] if x % 2 != 0]
    else:
        return [x for x in numbers[:-1] if x % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
