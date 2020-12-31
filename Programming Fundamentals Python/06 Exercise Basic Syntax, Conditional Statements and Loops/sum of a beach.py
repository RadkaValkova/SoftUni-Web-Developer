word = input().lower()

counter = 0

if 'water' in word:
    counter += word.count('water')
if 'fish' in word:
    counter += word.count('fish')
if 'sun' in word:
    counter += word.count('sun')
if 'sand' in word:
    counter += word.count('sand')

print(counter)

