n = int(input())
result = 1

for num in range (n, 0, -1):
    result *= num

print(result)


n = int(input())
fact = 1
while True:
    fact = fact * n
    n -= 1
    if not n > 1:
        break

