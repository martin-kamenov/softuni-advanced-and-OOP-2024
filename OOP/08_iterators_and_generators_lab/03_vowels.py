class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'y', 'u', 'o', 'i']
        self.vowels_to_string = [x for x in self.string if x.lower() in self.vowels]
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1

        if self.current_index < len(self.vowels_to_string):
            return self.vowels_to_string[self.current_index]

        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
