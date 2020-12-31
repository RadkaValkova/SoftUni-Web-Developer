import re

data = input()

pattern = r'(#|\|)(?P<name>[a-zA-Z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,5})\1'

matches = re.finditer(pattern,data)
total_calories = 0

for el in matches:
    total_calories += int(el.group('calories'))

print(f'You have food to last you for: {total_calories//2000} days!')
for el in re.finditer(pattern,data):
    print(f"Item: {el.group('name')}, Best before: {el.group('date')}, Nutrition: {el.group('calories')}")

