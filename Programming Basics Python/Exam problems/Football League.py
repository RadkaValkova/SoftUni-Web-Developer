capacity = int(input())
all_fans = int(input())
a = 0
b = 0
v = 0
g = 0

for i in range(1,all_fans +1):
    sector = input()
    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == 'V':
        v += 1
    else:
        g += 1

print(f'{a/all_fans*100:.2f}%')
print(f'{b/all_fans*100:.2f}%')
print(f'{v/all_fans*100:.2f}%')
print(f'{g/all_fans*100:.2f}%')
print(f'{(a+b+v+g)/capacity*100:.2f}%')