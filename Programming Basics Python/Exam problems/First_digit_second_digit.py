txt = '12345'

txt_first_digit = int(txt[:-4])
txt_third_digit = int(txt[2:-2])
txt_fifth_digit = int(txt[4:])

print(txt_first_digit)
print(txt_third_digit)
print(txt_fifth_digit)

#задачата дава информация как от стрингов низ от числа може да се извади конкретен знак
# text = input()
# letter = text[0] броенето започва от 0, т.е. първата буква ти е на 0-лева позеция, втората буква е на 1-ва позиция и т.н
# print(letter) ще отпечата съответната буква