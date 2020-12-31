import re

pattern = r'([=|\/])([A-Z][a-zA-Z]{2,})\1'
text = input()

matches = re.findall(pattern, text)
valid_destinations = [match[1] for match in matches]

travel_points = 0
for el in valid_destinations:
    travel_points += len(el)

print(f'Destinations: {", ".join(valid_destinations)}')
print(f'Travel Points: {travel_points}')