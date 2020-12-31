expected_gain = float(input())
sum_check = 0
total_cocktail_num = 0

while True:
    cocktail_name = input()
    if cocktail_name == 'Party!':
        print(f'We need {(expected_gain - sum_check):.2f} leva more.')
        break
    cocktail_number = int(input())
    cocktail_price = len(cocktail_name)
    check = cocktail_number * cocktail_price
    if check % 2 != 0:
        check = check * 0.75
    sum_check += check
    if sum_check >= expected_gain:
        print('Target acquired.')
        break
print(f'Club income - {sum_check:.2f} leva.')