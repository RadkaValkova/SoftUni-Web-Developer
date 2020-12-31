text = input()

result = ''

for i in range(len(text)):
    current_char = ord(text[i])
    new_char = chr(current_char+3)
    result += new_char

print(result)

# text = input()
#
# new = [chr(ord(text[i])+3) for i in range(len(text))]
# print(''.join(new))