collecting_items = input().split(', ')

while True:
    line = input()
    if line == 'Craft!':
        print(', '.join(collecting_items))
        break
    command, item = line.split(' - ')
    if command == 'Collect':
        if item not in collecting_items:
            collecting_items.append(item)
    elif command == 'Drop':
        if item in collecting_items:
            collecting_items.remove(item)
    elif command == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in collecting_items:
            index = collecting_items.index(old_item)
            collecting_items.insert(index+1, new_item)
        else:
            continue
    elif command == 'Renew':
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

