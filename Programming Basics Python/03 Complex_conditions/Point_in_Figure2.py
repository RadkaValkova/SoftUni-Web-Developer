h = int(input())  # 97 от 100 грешка на 19 и 20 проверка
x = int(input())
y = int(input())

in_figure1 = (x > 0 and x < 3*h and y > 0 and y < h)
in_fiqure2 = (x > h and x < 2*h and y > h and y < 4*h)
inside_borders = x == h and x == 2*h and y == 2*h and y == 3*h
# small borders =(y = h and x > h and x < 2*h) or (y = 2*h and x > h and x < 2*h)

out_figure1 = (y>h and x<h) or (y>4*h) or (y>h and x>2*h)
out_figure2 = x<0 or y<0 or x>3*h

if out_figure1 or out_figure2:
    print('outside')
elif in_figure1 or in_fiqure2:
    print('inside')
else:
    print('border')
