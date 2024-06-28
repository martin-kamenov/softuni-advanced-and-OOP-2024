coordinates = [[points for points in input().split('-')] for _ in range(int(input()))]

longest_intersection = 0
max_intersection_order = []

for coo in coordinates:
    first_start, first_end = [int(x) for x in coo[0].split(',')]
    second_start, second_end = [int(x) for x in coo[1].split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    if len(first_set.intersection(second_set)) > longest_intersection:
        max_intersection_order = first_set.intersection(second_set)
        longest_intersection = len(max_intersection_order)

print(f'Longest intersection is [{", ".join(str(s) for s in max_intersection_order)}] '
      f'with length {longest_intersection}')


# longest_intersection = {}
#
# for _ in range(int(input())):
#     first_range, second_range = [el.split(',') for el in input().split('-')]
#
#     first_start, first_end = int(first_range[0]), int(first_range[1])
#     second_start, second_end = int(second_range[0]), int(second_range[1])
#
#     first_set = set(range(first_start, first_end + 1))
#     second_set = set(range(second_start, second_end + 1))
#
#     intersection = first_set.intersection(second_set)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(
#     f'Longest intersection is '
#     f'[{", ".join(str(x) for x in longest_intersection)}] '
#     f'with length {len(longest_intersection)}'
# )
#
