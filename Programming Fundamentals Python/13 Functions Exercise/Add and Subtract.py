a = int(input())
b = int(input())
c = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    print(subtract(result, c))


add_and_subtract(a, b, c)
