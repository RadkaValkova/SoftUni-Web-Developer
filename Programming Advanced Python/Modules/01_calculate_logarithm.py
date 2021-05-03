from math import log
from termcolor import colored


def calc_log(x, base):
    if base == 'natural':
        return log(x)
    else:
        return log(x, int(base))


x = int(input())
base = input()

print(f'{calc_log(x, base):.2f}')
print(colored('Hello', 'green'))
