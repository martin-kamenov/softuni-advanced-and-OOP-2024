# class ValueCannotBeNegative(Exception):
#     pass
#
#
# try:
#     for _ in range(5):
#         num = int(input())
#
#         if num < 0:
#             raise ValueCannotBeNegative
#
#         print(num)
# except ValueCannotBeNegative:
#     print(f'Value cannot be negative number. Convert {num} to {abs(num)}')


class ValueCannotBeNegative(Exception):
    pass


numbers = [int(input()) for _ in range(5)]

for num in numbers:
    if num < 0:
        raise ValueCannotBeNegative(f'Value cannot be negative number. Convert {num} to {abs(num)}')