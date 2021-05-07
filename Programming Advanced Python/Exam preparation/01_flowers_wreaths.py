from collections import deque

lilies = deque(int(el) for el in input().split(', '))
roses = deque(int(el) for el in input().split(', '))
lilies = deque(list(reversed(lilies)))
wreaths = 0
store = []

while True:
    if lilies and roses:
        current_ros = roses[0]
        current_lil = lilies[0]
        if current_ros + current_lil == 15:
            wreaths += 1
            roses.popleft()
            lilies.popleft()
        elif current_ros + current_lil < 15:
            store.append(roses.popleft())
            store.append(lilies.popleft())
        elif current_ros + current_lil > 15:
            lilies[0] -= 2
    else:
        break
if wreaths + sum(store)//15 >=5:
    print(f'You made it, you are going to the competition with {wreaths + sum(store)//15} wreaths!')
else:
    print(f'You didn\'t make it, you need {5-(wreaths+ sum(store)//15)} wreaths more!')

