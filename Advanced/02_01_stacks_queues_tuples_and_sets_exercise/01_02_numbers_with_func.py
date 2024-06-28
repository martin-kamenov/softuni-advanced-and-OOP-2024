def add_func(current_set: set, data: list):
    [current_set.add(int(x)) for x in data]


def remove_func(current_set: set, data: list):
    [current_set.discard(int(x)) for x in data]


def check_subset(first: set, second: set):
    print(first.issubset(second) or second.issubset(first))


def print_func(first, second):
    print(*sorted(first), sep=", ")
    print(*sorted(second), sep=", ")


first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}

for _ in range(int(input())):
    action, action_, *current_data = input().split()
    command = action + " " + action_

    if command == "Add First":
        add_func(first_set, current_data)
    elif command == "Add Second":
        add_func(second_set, current_data)
    elif command == "Remove First":
        remove_func(first_set, current_data)
    elif command == "Remove Second":
        remove_func(second_set, current_data)
    elif command == "Check Subset":
        check_subset(first_set, second_set)

print_func(first_set, second_set)
