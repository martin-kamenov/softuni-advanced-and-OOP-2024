stack = []

functions = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(int(input())):
    numbers_data = [int(x) for x in input().split()]

    functions[numbers_data[0]](numbers_data)

print(*stack[::-1], sep=', ')


# from collections import deque
#
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None
# }
#
# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#
# numbers.reverse()
#
# print(*numbers, sep=', ')


# numbers = []
#
# for _ in range(int(input())):
#     numbers_data = [int(x) for x in input().split()]
#     command = int(numbers_data[0])
#
#     if command == 1:
#         numbers.append(numbers_data[1])
#     elif numbers:
#         if command == 2:
#             numbers.pop()
#         elif command == 3:
#             print(max(numbers))
#         elif command == 4:
#             print(min(numbers))
#
# numbers.reverse()
#
# print(*numbers, sep=', ')


# queries = int(input())
#
# numbers = []
#
# functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(queries):
#     user_command = [int(x) for x in input().split()]
#     functions[user_command[0]](user_command)
#
# print(*reversed(numbers), sep=', ')

