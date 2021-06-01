def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = {'a','e','o','u','i','y'}
        return [el for el in result if el.lower() in vowels]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
