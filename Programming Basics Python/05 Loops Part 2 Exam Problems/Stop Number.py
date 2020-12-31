n = int(input())   # 0 <=n < m
m = int(input())   # n < m <= 10000
s = int(input())   # спиращо число, да не се отпечатва

result = ''

for num in range (m, n-1, -1):
    if num % 2 == 0 and num % 3 == 0:
        if num == s:
           break
        result += f'{num} '
print(result)

