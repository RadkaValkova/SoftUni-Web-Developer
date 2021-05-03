with open('text.txt', 'r') as file:
    with open('output.txt', 'w') as file2:
        index = 1
        for line in file:
            letters = len([x for x in line if x.isalpha()])
            punctoation = len([x for x in line if not x.isalpha() and not x.isspace()])
            file2.writelines(f'Line {index}: {line.strip()} ({letters})({punctoation})\n')
            index += 1