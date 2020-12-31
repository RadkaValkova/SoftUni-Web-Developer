# n = int(input())
#
# for i in range(1, n+1):
#     print(i*'*')
# for i in range(n-1, 0, -1):
#     print(i*'*')

GROW = 1
SHRINK = -1

desired_size = int(input())
step = GROW
current_size = 0

while(current_size < desired_size and step == GROW) or (step == SHRINK and current_size > 0):
    current_size += step
    print('*' * current_size)
    if desired_size == current_size:
        step = SHRINK