def squares(n):
    for index in range(1, n + 1):
        yield index ** 2

print(list(squares(5)))