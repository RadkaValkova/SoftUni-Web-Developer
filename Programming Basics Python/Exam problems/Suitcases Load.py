trunk_volume = float(input())
counter = 0
sum_suitcase_volume = 0
while True:
    line = input()
    if line == 'End':
        print('Congratulations! All suitcases are loaded!')
        break
    suitcase_volume = float(line)
    sum_suitcase_volume += suitcase_volume
    if trunk_volume <= sum_suitcase_volume:
        print('No more space!')
        break
    else:
        counter += 1
        if counter % 3 == 0:
            suitcase_volume = suitcase_volume * 1.1
print(f'Statistic: {counter} suitcases loaded.')
