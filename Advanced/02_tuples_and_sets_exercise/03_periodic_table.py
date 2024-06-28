number = int(input())
set_of_elements = set()

for _ in range(number):
    elements = input().split()
    [set_of_elements.add(el) for el in elements]

print(*set_of_elements, sep='\n')

# table = set()
#
# for _ in range(int(input())):
#     for el in input().split():  # input().split() -> ["Ce", "O", "H"]
#         table.add(el)
#
# print(*table, sep="\n")


# elements = set()
#
# for _ in range(int(input())):
#     curr_elements = input().split()
#
#     for el in curr_elements:
#         elements.add(el)
#
# print(*elements, sep="\n")
#
#
# elements = set()
#
# for _ in range(int(input())):
#     current_elements = input().split()
#
#     for el in current_elements:
#         elements.add(el)
#
# print(*elements, sep='\n')
