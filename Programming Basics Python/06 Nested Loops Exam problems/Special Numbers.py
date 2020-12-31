N = int(input())
counter = 0

for i in range(1111, 10000):
    number = i
    result = 0
    counter = 0
    for position in range(1, 4+1):
        digit = number % 10
        number = number // 10
        if digit != 0:
            result = N % digit
            if result == 0:
                counter += 1

    if counter == 4:
        print(i, end=' ')
