necessary_honey = float(input())
total_honey = 0

while True:
    name = input()
    if name == 'Winter has come':
        if total_honey >= necessary_honey:
            print(f'Well done! Honey surplus {(total_honey - necessary_honey):.2f}.')
        else:
            print(f'Hard Winter! Honey needed {(necessary_honey - total_honey):.2f}.')
        break

    individual_honey = 0

    for i in range(1, 6 + 1):
        honey = float(input())
        individual_honey += honey
    if individual_honey < 0:
        print(f'{name} was banished for gluttony')
    total_honey += individual_honey

    if total_honey >= necessary_honey:
        print(f'Well done! Honey surplus {(total_honey - necessary_honey):.2f}.')
        break


