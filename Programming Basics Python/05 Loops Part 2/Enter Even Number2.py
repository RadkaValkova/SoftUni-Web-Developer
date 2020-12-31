n = int(input('Enter even number: '))

while True:
    print('Enter even number: ')
    n = int(input('Enter even number: '))
    if n % 2 == 0:
        break
    print(f'Even number entred: {n}')
print('The number is not even.')

