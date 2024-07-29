# class Fibonacci:
#     def __init__(self):
#         self.cache = {}
#
#     def __call__(self, num):
#         if num not in self.cache:
#             if num == 0:
#                 self.cache[0] = 0
#             elif num == 1:
#                 self.cache[1] = 1
#             else:
#                 self.cache[num] = self(num - 1) + self(num - 2)
#
#         return self.cache[num]
#
#
# fib = Fibonacci()
# for i in range(7):
#     print(fib(i))
#
# print(fib.cache)


# def can_climb(a) -> bool:
#     if a >= 100:
#         return True
#
#     return False
#
# print(can_climb(50))

# a = ['1', '2', '3']
# b = ['1', '2', '3', '4']
#
# print(set(b).symmetric_difference(a))

def param(strength, difficulty_level):
    strength = strength - 20 * 2 if difficulty_level == "Extreme" else strength - 20 * 1.5

    print(strength)

param(200, "Extreme")