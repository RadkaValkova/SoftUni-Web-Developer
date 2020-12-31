text = input()
len_tex = len(text)

sum = 0

for char in range(0, len_tex):
    current_char = text[char]
    if current_char == 'a':
        sum += 1
    elif current_char == 'e':
        sum += 2
    elif current_char == 'i':
        sum += 3
    elif current_char == 'o':
        sum += 4
    elif current_char == 'u':
        sum += 5
print(sum)




