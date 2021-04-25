def positive_numbers(numbers):
    return f'Positive: {", ".join(x for x in numbers if int(x) >= 0)}'


def negative_numbers(numbers):
    return f'Negative: {", ".join(x for x in numbers if int(x) < 0)}'


def even_numbers(numbers):
    return f'Even: {", ".join(x for x in numbers if int(x) % 2 == 0)}'


def odd_numbers(numbers):
    return f'Odd: {", ".join(x for x in numbers if int(x) % 2 == 1)}'


numbers = input().split(', ')

function_list = [positive_numbers(numbers),negative_numbers(numbers),even_numbers(numbers),odd_numbers(numbers)]

[print(el) for el in function_list]