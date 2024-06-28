# names = set()
#
# for _ in range(int(input())):
#     name = input()
#     names.add(name)
#
# for name in names:
#     print(name)

names_data = {input() for _ in range(int(input()))}

for name in names_data:
    print(name)


# names = {input() for _ in range(int(input()))}
# print(*names, sep="\n")


# names = set()
#
# for _ in range(int(input())):
#     name = input()
#     names.add(name)
#
# print(*names, sep="\n")


# names = set()
#
# for _ in range(int(input())):
#     names.add(input())
#
# [print(name, sep='\n') for name in names]