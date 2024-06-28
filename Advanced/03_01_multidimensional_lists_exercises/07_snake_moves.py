from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")


# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
# text = deque(input())
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([''] * cols)
#
#     for col in range(cols):
#         if row % 2 == 0:
#             matrix[row][col] = text[0]
#         else:
#             matrix[row][-1 - col] = text[0]
#
#         text.rotate(-1)
#
# [print(*row, sep='') for row in matrix]
