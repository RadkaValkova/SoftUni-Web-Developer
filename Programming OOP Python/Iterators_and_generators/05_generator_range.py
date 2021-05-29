def genrange(start, end):
    number = start
    while number <= end:
        yield number
        number += 1

print(list(genrange(1, 10)))