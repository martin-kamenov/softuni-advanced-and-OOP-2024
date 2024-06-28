def words_sorting(*words):
    words_dict = {}
    result = []
    sorted_words = []

    for word in words:
        word_ascii_value = 0

        for char in range(len(word)):
            word_ascii_value += ord(word[char])

        words_dict[word] = word_ascii_value

    if sum(words_dict.values()) % 2 != 0:
        sorted_words = sorted(words_dict.items(), key=lambda x: -x[1])
    else:
        sorted_words = sorted(words_dict.items(), key=lambda x: x[1])

    for curr_word, value in sorted_words:
        result.append(f'{curr_word} - {value}')

    return '\n'.join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
