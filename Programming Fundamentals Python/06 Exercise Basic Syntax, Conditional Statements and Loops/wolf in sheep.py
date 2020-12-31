queue = input().split(', ')

for i in range(len(queue), -1, -1):
    if queue[-1] == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif queue[-i] == 'wolf':
        print(f'Oi! Sheep number {abs(-i + 1)}! You are about to be eaten by a wolf!')
        break
