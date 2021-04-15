clothes_in_box = input()
rack_capacity = int(input())

clothes = [int(x) for x in clothes_in_box.split(' ')]

rack = 0
rack_counter = 0
while clothes:
    current_clothe = clothes.pop()
    if rack + current_clothe < rack_capacity:
        rack += current_clothe
    elif rack + current_clothe == rack_capacity:
        rack += current_clothe
        rack_counter += 1
        rack = 0
    elif rack + current_clothe > rack_capacity:
        rack_counter += 1
        rack = current_clothe
if rack > 0:
    rack_counter += 1

print(rack_counter)


