animal = input()
type = 0

if animal == 'dog':
    type = 'mammal'
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    type = 'reptile'
else:
    type = 'unknown'

print(type)