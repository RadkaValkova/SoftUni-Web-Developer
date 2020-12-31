while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    sum_saving = 0
    while True:
        saving = float(input())
        sum_saving += saving
        if sum_saving >= budget:
            print(f'Going to {destination}!')
            break

