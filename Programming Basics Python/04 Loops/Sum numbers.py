n = int(input())
sum = 0

for number in range (1,n+1):
    input_number = int(input())
    sum = input_number + sum       # това може да се запише sum += input_number

print(sum)