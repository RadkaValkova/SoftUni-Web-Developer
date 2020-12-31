n = int(input())
a = 0
b = 0
c = 0
d = 0
result = ''

for num in range(1111, 9999 + 1):
    a = num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    c = num % 10
    num = num // 10
    d = num
    if a != 0 and b != 0 and c != 0 and d != 0:
        if n % a == 0 and n % b == 0 and n % c == 0 and n % d == 0:
            result += f'{d}{c}{b}{a} '
print(result)
