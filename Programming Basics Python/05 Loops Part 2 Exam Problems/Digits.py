n = int(input())

first = n // 100
second = (n // 10) % 10
third = n % 10
result = ''
N = first + second
M = first + third
for row in range(1, N+1):
    for col in range(1, M+1):
        if n % 5 == 0:
            n = n - first
            print(n, end=' ')
        elif n % 3 == 0:
            n = n - second
            print(n, end=' ')
        else:
            n = n + third
            print(n, end=' ')
    print()









