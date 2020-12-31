groceries = input().split('!')


while True:
    line = input()
    if line == 'Go Shopping!':
        print(", ".join(groceries))
        break
    command = line.split()[0]

    if command == 'Urgent':
        item = line.split()[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif command == 'Unnecessary':
        item = line.split()[1]
        if item in groceries:
            groceries.remove(item)

    elif command == 'Correct':
        old_item, new_item = line.split()[1], line.split()[2]
        if old_item in groceries:
            # groceries.insert(groceries.index(old_item), new_item)
            # groceries.remove(old_item)
            index_old_item = groceries.index(old_item)
            groceries[index_old_item] = new_item

    elif command == 'Rearrange':
        item = line.split()[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)
