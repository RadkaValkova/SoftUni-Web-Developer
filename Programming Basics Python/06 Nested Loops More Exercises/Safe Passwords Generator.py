a = int(input())
b = int(input())
max_password_number = int(input())
                                         # не е решена
password_counter = 0

for A in range(35,55+1):
    for B in range(64, 96+1):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|', end='')
                while True:
                    password_counter += 1
                    if password_counter == max_password_number:
                        break