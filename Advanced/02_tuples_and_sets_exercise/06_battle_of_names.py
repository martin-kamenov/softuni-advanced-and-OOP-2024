odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name = sum(ord(letter) for letter in input()) // row

    if name % 2 == 0:
        even_set.add(name)
    else:
        odd_set.add(name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
