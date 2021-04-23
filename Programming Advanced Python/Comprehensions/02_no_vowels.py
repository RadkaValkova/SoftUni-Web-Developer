text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

filtered = [x for x in text if x.lower() not in vowels]
print(''.join(filtered))