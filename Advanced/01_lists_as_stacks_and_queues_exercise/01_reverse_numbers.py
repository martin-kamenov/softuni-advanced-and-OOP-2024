# from collections import deque
#
# numbers = deque(input().split())
# numbers.reverse()
#
# print(' '.join(numbers))


print(*input().split()[::-1], sep=' ')

# [print(el, end=" ")for el in reversed(input().split())]


# stack_of_numbers = [int(x) for x in input().split()]
#
# while stack_of_numbers:
#     print(stack_of_numbers.pop(), end=' ')