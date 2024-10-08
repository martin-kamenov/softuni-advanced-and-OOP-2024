def type_check(curr_type):

    def decorator(func):

        def wrapper(*args):
            if not isinstance(*args, curr_type):
                return "Bad Type"

            return func(*args)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
