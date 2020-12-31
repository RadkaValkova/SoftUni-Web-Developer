n = int(input())

synonyms_dict = {}

words = [input() for word in range(2*n)]
for i in range(0, len(words), 2):
    key_word = words[i]
    synonym = words[i+1]

    if key_word not in synonyms_dict:
        synonyms_dict[key_word] = []

    synonyms_dict[key_word].append(synonym)

for (word,synonym) in synonyms_dict.items():
    print(f'{word} - {", ".join(synonym)}')
