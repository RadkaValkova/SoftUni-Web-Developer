prime_sum = 0
non_prime_sum = 0

line = input()
while line != 'stop':
    current_number = int(line)
    if current_number < 0:
        print('Number is negative.')
        line = input()
        continue

    counter = 0
    for i in range(1, current_number+1):
        if current_number % i == 0:
            counter += 1

    if counter == 2:
        prime_sum += current_number
    else:
        non_prime_sum += current_number
    line = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')