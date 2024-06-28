from string import punctuation

with open('text.txt') as file:
    text = file.readlines()

with open('output.txt', 'w') as file:
    for line, content in enumerate(text):
        words = 0
        punctuation_signs = 0

        for char in content:
            if char in punctuation:
                punctuation_signs += 1
            elif char.isalpha():
                words += 1

        file.write(f'Line {line + 1}: {content.strip()} ({words})({punctuation_signs})\n')
