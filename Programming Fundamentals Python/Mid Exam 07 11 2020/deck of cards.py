cards = input().split(', ')
n = int(input())

for i in range(n):
    tokens = input().split(', ')
    command = tokens[0]

    if command == 'Add':
        card_name = tokens[1]
        if card_name in cards:
            print('Card is already bought')
        else:
            print('Card successfully bought')
            cards.append(card_name)

    elif command == 'Remove':
        card_name = tokens[1]
        if card_name in cards:
            print('Card successfully sold')
            cards.remove(card_name)
        else:
            print('Card not found')

    elif command == 'Remove At':
        index = int(tokens[1])
        if index not in range(len(cards)):
            print('Index out of range')
        else:
            print('Card successfully sold')
            cards.pop(index)

    elif command == 'Insert':
        index = int(tokens[1])
        card_name = tokens[2]
        if index not in range(len(cards)):
            print('Index out of range')
        elif index in range(len(cards)) and card_name not in cards:
            print('Card successfully bought')
            cards.insert(index, card_name)
        elif index in range(len(cards)) and card_name in cards:
            print('Card is already bought')


print(', '.join(cards))