key = int(input())
number_of_lines = int(input())

for i in range(number_of_lines):
    current_letter = input()
    letter_value = ord(current_letter) + key
    new_letter = chr(letter_value)
    print(new_letter, end='')

# key = int(input())
# n = int(input())
# word = ""
# for _ in range(n):
#     char = input()
#     word += chr(ord(char) + key)
#
# print(word)
