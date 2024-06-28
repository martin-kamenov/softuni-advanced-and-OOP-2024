data = input()

indexes = []

for index in range(len(data)):
    char = data[index]

    if char == '(':
        indexes.append(index)
    elif char == ')':
        start_index = indexes.pop()
        print(data[start_index:index + 1])
