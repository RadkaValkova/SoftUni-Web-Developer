import sys
divisor = int(input())
bound = int(input())
divided_N = 0
max_N = -sys.maxsize

for i in range(1,bound+1):
    if i % divisor == 0:
        divided_N = i
    if divided_N > max_N:
        max_N = divided_N
print(max_N)