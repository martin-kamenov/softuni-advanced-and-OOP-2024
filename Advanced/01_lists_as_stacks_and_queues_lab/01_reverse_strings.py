string = list(input())

for char in range(len(string)):
    removed = string.pop()
    print(removed, end='')

# while len(string) > 0:
#     element = string.pop()
#     print(element, end='')


# text = input()
# result = []
#
# for index in range(len(text)):
#     result.append(text[index])
#
# print(''.join(result[::-1]))
