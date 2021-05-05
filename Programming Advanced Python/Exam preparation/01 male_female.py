from collections import deque


def removing_zeroes_and_less(ll):
    return [el for el in ll if el > 0]


def remove_divisible_to_25(males,females):
    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
    if females[0] % 25 == 0:
        females.popleft()
        if females:
            females.popleft()
    return males,females


males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
matches_counter = 0

while True:
    males = deque(removing_zeroes_and_less(males))
    females = deque(removing_zeroes_and_less(females))
    if len(males) <= 0 or len(females) <= 0:
        break
    males,females = remove_divisible_to_25(males,females)
    if females[0] == males[-1]:
        females.popleft()
        males.pop()
        matches_counter += 1
    else:
        females.popleft()
        males[-1] -= 2


print(f'Matches: {matches_counter}')
if males:

    print(f'Males left: {", ".join(str(el) for el in reversed(males))}')
else:
    print('Males left: none')

if females:
    print(f'Females left: {", ".join(str(el) for el in females)}')
else:
    print('Females left: none')