n = int(input('Enter even number: '))

while n % 2 != 0:
    print('The number is not even.')
    n = int(input('Enter even number: '))
else:
    print(f'Even number entred: {n}')