import re

coolness = 1
emoji = []
coolest_emoji = []

text = input()
for x in text:
    if x.isdigit():
        coolness *= int(x)

pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,}\1)'
matches = re.finditer(pattern, text)
for match in matches:
    emoji.append(match[0].strip())
for element in emoji:
    emoji_value = 0
    for i in range(2,len(element)-2):
        emoji_value += ord(element[i])
    if emoji_value > coolness:
        coolest_emoji.append(element)

print(f'Cool threshold: {coolness}')
print(f'{len(emoji)} emojis found in the text. The cool ones are:')
for el in coolest_emoji:
    print(el)



