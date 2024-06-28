line = input().split("|")

sub_lists = []

for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)


#solution 2

# numbers = [string.split() for string in input().split("|")]
# print(*[" ".join(sub_list) for sub_list in numbers[::-1] if sub_list])


# matrix = input().split('|')
# flatten_list = [row.split() for row in matrix]
# revers = flatten_list[::-1]
#
# print(*[' '.join(sub_list) for sub_list in revers if sub_list])
