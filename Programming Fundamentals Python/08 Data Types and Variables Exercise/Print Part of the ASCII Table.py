start_index = int(input())
last_index = int(input())

for i in range(start_index, last_index + 1):
    current_symbol = chr(i)
    print(f'{current_symbol}', end=' ')