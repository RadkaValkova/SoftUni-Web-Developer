words = input().split()

while True:
    line = input()
    if line == 'Stop':
        break
    command = line.split()[0]
    if command == 'Delete':
        index = int(line.split()[1])
        if index+1 in range(len(words)) and index in range(len(words)):
            words.pop(index+1)

    elif command == 'Swap':
        word1 = line.split()[1]
        word2 = line.split()[2]
        if word1 in words and word2 in words:
            ind1 = words.index(word1)
            ind2 = words.index(word2)
            words[ind1], words[ind2] = words[ind2], words[ind1]

    elif command == 'Put':
        word = line.split()[1]
        index = int(line.split()[2])
        if index in range(len(words)) and index-1 in range(len(words)):
            words.insert(index-1, word)

    elif command == 'Sort':
        words.sort(reverse=True)

    elif command == 'Replace':
        word1 = line.split()[1]
        word2 = line.split()[2]
        if word2 in words:
            ind2 = words.index(word2)
            words[ind2] = word1

print(' '.join(words))