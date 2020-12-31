first = int(input())
second = int(input())
third = int(input())

sum = first + second + third
minutes = sum // 60
seconds = sum % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')