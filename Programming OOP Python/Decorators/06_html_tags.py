def tags(symbol):
    def inner(fn):
        def wrapper(*args):
            res = fn(*args)
            return f'<{symbol}>{res}</{symbol}>'
        return wrapper
    return inner


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))

