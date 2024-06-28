first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())


functions = {
    "Add First": lambda x: [first_sequence.add(int(el)) for el in x],
    "Add Second": lambda x: [second_sequence.add(int(el)) for el in x],
    "Remove First": lambda x: [first_sequence.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_sequence.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
}

for _ in range(int(input())):
    action, current_set, *data = input().split()
    command = action + " " + current_set

    functions[command](data)

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
