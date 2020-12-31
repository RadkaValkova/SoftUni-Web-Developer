a = int(input())
b = int(input())              # не успявам да я направя
c = int(input())


for first_digit in range(1, a+1):
    if first_digit % 2 != 0:
        continue
    counter = 0
    number = 0
    for second_digit in range(2, 7+1):
        number = second_digit
        if number % second_digit == 0:
            counter += 1

        for third_digit in range(1, c+1):
            if third_digit % 2 != 0:
                continue
            if counter == 2:
                second_digit = number

            print(f'{first_digit}{second_digit}{third_digit}')
