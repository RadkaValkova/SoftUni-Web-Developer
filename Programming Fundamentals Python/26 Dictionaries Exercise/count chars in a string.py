text_string = input()

characters_dict = {}

for letter in text_string:
    if letter != ' ':
        if letter not in characters_dict:
            characters_dict[letter] = 0
        characters_dict[letter] += 1

for (key,value) in characters_dict.items():
    print(f'{key} -> {value}')
