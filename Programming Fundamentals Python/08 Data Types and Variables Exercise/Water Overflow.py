n = int(input())
capacity = 255
sum_litters = 0

for i in range(n):
    litters = int(input())
    if sum_litters + litters > capacity:
        print('Insufficient capacity!')
    else:
        sum_litters += litters
print(sum_litters)
