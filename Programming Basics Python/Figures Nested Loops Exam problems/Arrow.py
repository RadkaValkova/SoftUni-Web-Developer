n = int(input())
col = n*2-1
dash1 = n
dot = n//2
dash2 = (col-n+2)//2
down_outside_dot = 1
down_inside_dot = col - down_outside_dot*2 - 2

print('.'*dot + '#'*dash1 + '.'*dot)

for row in range (1, (n-2)+1):
    print('.'*dot + '#' + '.'*(n-2) + '#'+ '.'*dot)

print('#'*dash2 + '.'*(n-2) + '#'*dash2)

for row in range (1, (n-2) +1):
    print('.'*down_outside_dot + '#' + '.'*down_inside_dot + '#' + '.'*down_outside_dot)
    down_outside_dot +=1
    down_inside_dot -=2

print('.'*(n-1) + '#' + '.'*(n-1))


