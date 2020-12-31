inventory = input().split(', ')

command = input()

while command != 'Craft!':
    command_list = command.split(' - ')
    action = command_list[0]

    if action == 'Collect':
        if command_list[1] not in inventory:
            inventory.append(command_list[1])
    if action == 'Drop':
        if command_list[1] in inventory:
            inventory.remove(command_list[1])
    if action == 'Combine Items':
        new_items = command_list[1].split(':')
        old_item = new_items[0]
        new_item = new_items[1]
        if old_item in inventory:
            new_index = inventory.index(old_item) + 1
            inventory.insert(new_index, new_item)
    if action == 'Renew':
        if command_list[1] in inventory:
            inventory.remove(command_list[1])
            inventory.append(command_list[1])

    command = input()

print(', '.join(inventory))