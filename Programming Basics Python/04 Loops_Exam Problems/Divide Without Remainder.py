n = int(input())
p1 = 0
p2 = 0
p3 = 0

for i in range (1,n+1):
    input_number = int(input())
    if input_number % 2 == 0:
        p1 += 1
    if input_number % 3 == 0:
        p2 += 1
    if input_number % 4 == 0:
        p3 += 1

print(f'{p1/n*100:.2f}%')
print(f'{p2/n*100:.2f}%')
print(f'{p3/n*100:.2f}%')