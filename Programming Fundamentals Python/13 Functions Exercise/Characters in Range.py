first_char = input()
last_char = input()


def chars_between_two(first, last):
    list_of_chars = []
    for i in range(ord(first)+1, ord(last)):
        current_char = chr(i)
        list_of_chars.append(current_char)
    return ' '.join(list_of_chars)


print(chars_between_two(first_char, last_char))