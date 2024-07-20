def reverse_text(string: str):

    for el in string[::-1]:
        yield el

for char in reverse_text("step"):
    print(char, end='')
