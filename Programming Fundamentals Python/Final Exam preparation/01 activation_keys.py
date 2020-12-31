raw_key = input()

while True:
    line = input()
    if line == 'Generate':
        break
    command = line.split('>>>')[0]
    if command == 'Contains':
        substring = line.split('>>>')[1]
        if substring in raw_key:
            print(f'{raw_key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        letter_case = line.split('>>>')[1]
        start_index = int(line.split('>>>')[2])
        end_index = int(line.split('>>>')[3])

        if letter_case == 'Upper':
            piece = raw_key[start_index:end_index]
            raw_key = raw_key.replace(piece, piece.upper())
            print(raw_key)
        else:
            piece = raw_key[start_index:end_index]
            raw_key = raw_key.replace(piece, piece.lower())
            print(raw_key)

    elif command == 'Slice':
        start_index = int(line.split('>>>')[1])
        end_index = int(line.split('>>>')[2])
        piece = raw_key[start_index:end_index]
        raw_key = raw_key.replace(piece, '')
        print(raw_key)

print(f'Your activation key is: {raw_key}')