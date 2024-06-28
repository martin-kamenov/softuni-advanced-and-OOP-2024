# def age_assignment(*names, **person_data):
#     result = []
#
#     for letter, age in person_data.items():
#         for name in names:
#             if name[0] == letter:
#                 result.append(f'{name} is {age} years old.')
#                 break
#
#     return '\n'.join(sorted(result))


# def age_assignment(*names, **data):
#     result = []
#
#     for letter, age in data.items():
#         for name in names:
#             if name[0].startswith(letter):
#                 result.append(f'{name} is {age} years old.')
#
#     return '\n'.join(sorted(result))

def age_assignment(*names, **kwargs):
    persons = {}

    for name in names:
        persons[name] = kwargs[name[0]]

    # persons = {name:kwargs[name[0]] for name in args}

    persons = sorted(persons.items())

    result = []
    for name, age in persons:
        result.append(f'{name} is {age} years old.')

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))