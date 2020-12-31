clients = int(input())
all_sum = 0
for i in range(1, clients + 1):
    counter = 0
    total_sum = 0
    while True:
        decoration = input()
        if decoration == 'Finish':
            if counter % 2 == 0:
                total_sum = total_sum * 0.8
            print(f'You purchased {counter} items for {total_sum:.2f} leva.')
            break
        if decoration == 'basket':
            total_sum += 1.50
            counter += 1
        elif decoration == 'wreath':
            total_sum += 3.80
            counter += 1
        elif decoration == 'chocolate bunny':
            total_sum += 7.00
            counter += 1
    all_sum += total_sum
print(f'Average bill per client is: {(all_sum / clients):.2f} leva.')
