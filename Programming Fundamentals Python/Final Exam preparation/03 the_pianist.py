n = int(input())

pieces = {}

for i in range(n):
    line = input()
    piece, composer, key = line.split('|')
    if piece not in pieces:
        pieces[piece] = {'composer': '', 'key': ''}
    pieces[piece]['composer'] = composer
    pieces[piece]['key'] = key

while True:
    line = input()
    if line == 'Stop':
        break
    tokens = line.split('|')
    command = tokens[0]
    if command == 'Add':
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        if piece not in pieces:
            pieces[piece] = {'composer': '', 'key': ''}
            pieces[piece]['composer'] = composer
            pieces[piece]['key'] = key
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif command == 'Remove':
        piece = tokens[1]
        if piece in pieces:
            pieces.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif command == 'ChangeKey':
        piece = tokens[1]
        new_key = tokens[2]
        if piece in pieces:
            pieces[piece]['key'] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

for key,value in sorted(pieces.items(), key= lambda x: (x[0],x[1]['composer'])):
    print(f'{key} -> Composer: {value["composer"]}, Key: {value["key"]}')
