import re

with open('words.txt') as file:
    words = file.read()

words = words.split()

with open('text.txt') as file:
    text = file.read()

words_count = {}

for word in words:
    pattern = rf'\b{word}\b'
    result = re.findall(pattern, text, re.IGNORECASE)
    words_count[word] = len(result)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open('output.txt', 'w') as file:
    for key, value in sorted_words_count:
        file.write(f'{key} - {value}\n')