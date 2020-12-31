num1 = int(input())
num2 = int(input())


def factorial_division(num1, num2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, num1 + 1):
        factorial1 = factorial1 * i
    for y in range(1, num2 + 1):
        factorial2 = factorial2 * y
    result = factorial1 / factorial2
    return f'{result:.2f}'


print(factorial_division(num1, num2))
