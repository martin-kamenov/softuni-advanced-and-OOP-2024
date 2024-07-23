def vowel_filter(function):

    def wrapper():
        result = function()
        vowels_result = [el for el in result if el.lower() in 'aeioyu']

        return vowels_result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
