expected_sum = int(input())

collected_sum = 0
collected_sum_cash = 0
collected_sum_card = 0
transaction = ''
transaction_count = 0
transaction_cash_count = 0
transaction_card_count = 0

while collected_sum < expected_sum:
    transaction = input()
    transaction_count += 1
    if transaction == 'End':
        print('Failed to collect required money for charity.')
        break
    if transaction_count % 2 != 0:
        if int(transaction) <= 100:
            print('Product sold!')
            collected_sum_cash += int(transaction)
            transaction_cash_count += 1
        else:
            print('Error in transaction!')
    elif transaction_count % 2 == 0:
        if int(transaction) >= 10:
            print('Product sold!')
            collected_sum_card += int(transaction)
            transaction_card_count += 1
        else:
            print('Error in transaction!')

    collected_sum = collected_sum_cash + collected_sum_card
    if collected_sum >= expected_sum:
        print(f'Average CS: {collected_sum_cash / transaction_cash_count:.2f}')
        print(f'Average CC: {collected_sum_card / transaction_card_count:.2f}')
