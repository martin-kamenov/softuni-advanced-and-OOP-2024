from collections import deque

lines = input()
queue = deque()

while lines != 'End':

    if lines == 'Paid':
        while queue:
            client = queue.popleft()
            print(client)
    else:
        queue.append(lines)

    lines = input()

print(f'{len(queue)} people remaining.')


# from collections import deque
#
# queue = deque()
#
# while True:
#
#     lines = input()
#
#     if lines == 'End':
#         print(f'{len(queue)} people remaining.')
#
#     elif lines == 'Paid':
#         while queue:
#             client = queue.popleft()
#             print(client)
#     else:
#         queue.append(lines)
