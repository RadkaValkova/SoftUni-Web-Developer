def debug(func):

    def wrapper(*args, **kwargs):
        args_str = ', '.join(args)
        kwargs_str = ', '.join(f'{key}={value}' for key, value in kwargs.items())
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args_str},{kwargs_str}) returned {result}')
        return result
    return wrapper

@debug
def sey_hello(name):
    return f'Hello,{name}'

print(sey_hello('Mimi'))