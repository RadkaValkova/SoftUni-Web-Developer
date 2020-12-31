number = int(input())


def perfect_number(number):
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    if result != number:
        return 'It\'s not so perfect.'
    else:
        return 'We have a perfect number!'


print(perfect_number(number))