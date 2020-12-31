import math
people_number = int(input())
enter_tax = float(input())
sheslong = float(input())
umbrella = float(input())

tax = people_number*enter_tax
sheslong_tax = math.ceil(people_number*0.75) * sheslong
umbrella_tax = math.ceil(people_number/2) * umbrella

total_sum = tax + sheslong_tax + umbrella_tax
print(f'{total_sum:.2f} lv.')