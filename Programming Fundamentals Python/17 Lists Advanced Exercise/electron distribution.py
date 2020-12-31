electron_numbers = int(input())

sum_sells = []
index = 1
while electron_numbers > 0:
    current_sell = 2*(index ** 2)
    if electron_numbers >= current_sell:
        current_sell = current_sell
        index += 1
    else:
        current_sell = electron_numbers
    electron_numbers -= current_sell
    sum_sells.append(current_sell)

print(sum_sells)