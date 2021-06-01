def type_check(t):
    def inner(fn):
        def wrapper(*args):
            if type(*args) == t:
                res = fn(*args)
                return res
            else:
                return 'Bad Type'
        return wrapper
    return inner


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

