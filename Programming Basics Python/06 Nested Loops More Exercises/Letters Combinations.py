first = input()
second = input()
third = input()
counter = 0

for first_digit in range(ord(first), ord(second)+1):
    for second_digit in range(ord(first), ord(second)+1):
        for third_digit in range(ord(first), ord(second)+1):
            if first_digit != ord(third) and second_digit != ord(third) and third_digit != ord(third):
                counter += 1
                print(f'{chr(first_digit)}{chr(second_digit)}{chr(third_digit)}', end=' ')
print(counter)