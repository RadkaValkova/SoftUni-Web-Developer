import math
figure = input()
area = 0

if figure == 'square':
    a = float(input())
    area = ('%.3f'% (a*a))

elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    area = ('%.3f'% (a*b))

elif figure == 'circle':
    r = float(input())
    area = ('%.3f'% (math.pi*r*r))

elif figure == 'triangle':
    a = float(input())
    h = float(input())
    area = ('%.3f'% (a*h/2))

print(area)
