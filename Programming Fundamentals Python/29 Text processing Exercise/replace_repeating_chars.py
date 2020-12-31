text = input()

index = 0
while index < len(text)-1:
    current_letter = text[index]
    next_letter = text[index+1]
    if current_letter == next_letter:
        text = text.replace(f'{current_letter}{next_letter}', f'{current_letter}')
        index = 0
    else:
        index += 1
print(text)

# text = input()
# result = ''
#
# for i in range(len(text)-1):
#     if text[i] != text[i+1]:
#         result += text[i]
# if text[-1] == text[-2]:
#     result += text[-2]
# else:
#     result += text[-1]
#
# print(result)