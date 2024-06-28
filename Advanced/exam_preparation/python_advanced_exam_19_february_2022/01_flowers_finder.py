from collections import deque

desired_words = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}
vowels = deque(input().split())
consonants = input().split()

found_words = []

while vowels and consonants:
    vowel_ = vowels.popleft()
    consonant_ = consonants.pop()

    for word in desired_words.keys():
        desired_words[word] = desired_words[word].replace(vowel_, '')
        desired_words[word] = desired_words[word].replace(consonant_, '')

        if desired_words[word] == '':
            print(f"Word found: {word}")
            break
    else:
        continue

    break
else:
    print('Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(consonants)}')