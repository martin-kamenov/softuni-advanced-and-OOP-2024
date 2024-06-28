from string import punctuation

with open('text.txt') as file:
    sentences = file.readlines()

for index, line in enumerate(sentences):
    if index % 2 == 0:

        for symbol in punctuation:
            line = line.replace(symbol, '@')

        print(' '.join(reversed(line.split())))
