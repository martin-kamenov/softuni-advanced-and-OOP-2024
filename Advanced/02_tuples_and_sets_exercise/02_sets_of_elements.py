first_len, second_len = [int(x) for x in input().split()]
first_set = {int(input()) for _ in range(first_len)}
second_set = {int(input()) for _ in range(second_len)}
print(*first_set.intersection(second_set), sep='\n')


# length_sets = [int(x) for x in input().split()]
# first_set = {input() for _ in range(length_sets[0])}
# second_set = {input() for _ in range(length_sets[1])}
# print(*first_set.intersection(second_set), sep="\n")


# first, second = [int(x) for x in input().split()]
#
# first_set = {int(input()) for _ in range(first)}
# second_set = {int(input()) for _ in range(second)}
#
# unique_elements = first_set.intersection(second_set)
# print(*unique_elements, sep='\n')