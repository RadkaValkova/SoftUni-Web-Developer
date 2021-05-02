import re

def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split(' ')


def get_words_counts(file_path, words):
    words_counts = {word: 0 for word in words}

    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = re.findall(r'[A-Za-z0-9]+', line.lower(), re.IGNORECASE)
            for word in words:
                words_counts[word] += words_in_line.count(word)

    return words_counts


file_path_words = '/13_file_handling/files/Words Count/words.txt'
file_path_text = '/13_file_handling/files/Words Count/text.txt'

words_counts = get_words_counts(file_path_text, get_words(file_path_words))

for key, value in sorted(words_counts.items(), key= lambda pair: -pair[1]):
    print(f'{key} - {value}')

