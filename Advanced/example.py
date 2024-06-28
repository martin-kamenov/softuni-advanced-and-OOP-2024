def recursive(num, symbol="*"):
    if num == 0:
        symbol = '#'
        return 1, symbol

    return symbol * recursive(num - 1)


print(recursive(5))