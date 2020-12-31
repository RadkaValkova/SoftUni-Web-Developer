num = float(input())

in_range = (100 <= num <= 200) or num == 0

if not in_range:
    print('invalid')