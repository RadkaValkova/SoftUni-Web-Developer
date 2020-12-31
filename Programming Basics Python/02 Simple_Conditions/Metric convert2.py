number = float(input())
convert_from = input()
convert_to = input()

number_in_meters = 0    # избираме да конвертираме през метър т.е първо всичко, което се въвежда превръщаме в метри

if convert_from == 'mm':
    number_in_meters = number / 1000
elif convert_from == 'cm':
    number_in_meters = number / 100
else:
    number_in_meters = number

result = 0                               # тук създаваме нова променлива, в която вече всичко, което сме превърнали
if convert_to == 'mm':                   # в метри и сме записали в конвърт ин метърс,  превръщаме
    result = number_in_meters * 1000     #  в изходната мерна единица
elif convert_to == 'cm':
    result = number_in_meters * 100
else:
    result = number_in_meters

print(f'{result:.3f}')