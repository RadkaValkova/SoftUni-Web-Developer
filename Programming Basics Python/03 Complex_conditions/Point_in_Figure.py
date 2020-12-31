h = int(input())
x = int(input())
y = int(input())

ins1 = x > 0 and  y > 0 and y < h and x != h and x != 2*h
ins2 = x < 3*h and y > 0 and y < h
ins3 = y < h and x> 0 and x < 3*h
ins4 = y > 0 and x> 0 and x < 3*h
ins5 = x > h and y > h and y < 4*h and y != 2*h and y != 3*h and y != h
ins6 = x < 2*h and y > h and y < 4*h
ins7 = y < 4*h and x > h and x < 2*h
ins8 = y > h and x > h and x < 2*h

on1 = (x == 0 or x == 3*h or x == h or x == 2*h) and (y >= 0 and y <= h)
on2 = (y == 0 or y == h) and x >= 0 and x <= 3*h
on3 = (y == 2*h or y == 3*h or y == 4*h) and x >= h and x <= 2*h
on4 = (x == h or x == 2*h) and y>=h and y <= 4*h

common_border = y = h and x > h and x < 2*h

if on1 or on2 or on3 or on4 or common_border:
    print('border')
elif (ins1 and ins2 and ins3 and ins4) or (ins5 and ins6 and ins7 and ins8):
    print('inside')
else:
    print('outside')

# излизат ми 92 точки, не намирам грешката

