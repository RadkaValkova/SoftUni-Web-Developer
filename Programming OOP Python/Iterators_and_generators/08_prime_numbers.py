from math import sqrt


def get_primes(ll):
    index = 0

    while index < len(ll):
        number = ll[index]
        is_prime = True
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime and number != 0 and number != 1:
            yield number
        index += 1


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


def is_prime(number):
    for x in range(2, int(sqrt(number) + 1)):
        if number % x == 0:
            return False
    return True


gg = (x for x in range(50) if is_prime(x))
print(list(gg))