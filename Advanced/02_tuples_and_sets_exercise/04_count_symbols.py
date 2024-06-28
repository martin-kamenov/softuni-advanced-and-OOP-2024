words = input()
symbols = {}

for symbol in words:
    symbols[symbol] = symbols.get(symbol, 0) + 1

for key, value in sorted(symbols.items()):
    print(f'{key}: {value} time/s')

# text = input()
#
# for symbol in sorted(set(text)):
#     print(f'{symbol}: {text.count(symbol)} time/s')


# text = list(input())
#
# for letter in sorted(set(text)):
#     print(f'{letter}: {text.count(letter)} time/s')
