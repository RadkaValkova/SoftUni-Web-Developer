numbers = input().split()
text = input()
text_string = [char for char in text]

get_chars = []

for num in numbers:
    num = [int(n) for n in num]
    index = sum(num)

    for char in text_string:
        if index > len(text_string):
            index = index % (len(text_string))
        get_chars.append(text_string[index])
        text_string.remove(text_string[index])
        break

print(''.join(get_chars))
