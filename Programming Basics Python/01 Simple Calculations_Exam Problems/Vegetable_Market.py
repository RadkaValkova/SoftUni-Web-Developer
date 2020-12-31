vegetable_price = float(input())
fruit_prce = float(input())
vegetable_weight = int(input())
fruit_weight = int(input())

total_value_lv = (vegetable_price*vegetable_weight)+(fruit_prce*fruit_weight)
total_value_EUR = (vegetable_price*vegetable_weight)+(fruit_prce*fruit_weight)/1.94

print(f'The amounth of the sells in EUR is {total_value_EUR}')
