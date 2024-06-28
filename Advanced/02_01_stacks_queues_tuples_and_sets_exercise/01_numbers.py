first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    action, current_set, *data = input().split()
    command = action + " " + current_set

    if command == "Add First":
        [first_sequence.add(int(x)) for x in data]
    elif command == "Add Second":
        [second_sequence.add(int(x)) for x in data]
    elif command == "Remove First":
        [first_sequence.discard(int(x)) for x in data]
    elif command == "Remove Second":
        [second_sequence.discard(int(x)) for x in data]
    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(", ".join(str(s) for s in sorted(first_sequence)))
print(", ".join(str(s) for s in sorted(second_sequence)))
