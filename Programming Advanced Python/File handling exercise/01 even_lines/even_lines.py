with open('text.txt', 'r') as file:
    symbols = ["-", ",", ".", "!", "?"]
    for (ind, line) in enumerate(file):
        if ind % 2 == 0:
            for el in symbols:
                line = line.replace(el, '@')
            reversed_words_in_line = reversed(line.strip().split(' '))
            print(' '.join(reversed_words_in_line))

