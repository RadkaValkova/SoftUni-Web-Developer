a1 = int(input())
a2 = int(input())
n = int(input())
m = int(n/2)
sign1 = ''
sign2 = 0
sign3 = 0
sign4 = 0
for number in range(a1,a2):
    sign1 = chr(number)
    for i in range(1,n):
        sign2 = i
        for y in range(1,m):
            sign3 = y
            for z in range(a1,a2):
                sign4 = ord(sign1)
            if sign4 % 2 != 0 and (sign2+sign3+sign4) % 2 != 0:
                print(f'{sign1}-{sign2}{sign3}{sign4}')