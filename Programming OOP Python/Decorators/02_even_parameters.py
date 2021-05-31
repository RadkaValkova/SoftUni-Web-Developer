def even_parameters(func):

    def wrapper(*args):
        if args:
            even_integers = [el for el in args if isinstance(el,int) and el % 2 == 0]
            if len(even_integers) == len(args):
                res = func(*args)
                return res
            else:
                return 'Please use only even numbers!'
        else:
            return func()
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))







