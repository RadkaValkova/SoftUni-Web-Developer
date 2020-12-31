first_number = int(input())
last_number = int(input())

for num in range(first_number,last_number+1):
    number = num
    sum_even_position = 0
    sum_odd_position = 0
    for position in range(1,6+1):
        digit = number % 10
        number = number // 10

        if position % 2 == 0:
            sum_even_position += digit
        if position % 2 != 0:
            sum_odd_position += digit

    if sum_even_position == sum_odd_position:
        print(num, end=' ')
