def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


numbers = [1, 2, 3]
print(multiply(numbers))