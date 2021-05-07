from collections import deque

first_box = deque([int(el) for el in input().split()])
second_box = [int(el) for el in input().split()]
claimed_items = []

while True:
    if not first_box:
        print('First lootbox is empty')
        break
    elif not second_box:
        print('Second lootbox is empty')
        break
    current_el_1 = first_box[0]
    current_el_2 = second_box[-1]
    if (current_el_1 + current_el_2) % 2 == 0:
        claimed_items.append(current_el_1 + current_el_2)
        first_box.popleft()
        second_box.pop()
    else:
        first_box.append(second_box.pop())

sum_claimed_items = sum(claimed_items)
if sum_claimed_items >= 100:
    print(f'Your loot was epic! Value: {sum_claimed_items}')
else:
    print(f'Your loot was poor... Value: {sum_claimed_items}')
