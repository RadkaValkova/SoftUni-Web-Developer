import sys
import math

word = input()
sum_letters_word = 0
max_word = -sys.maxsize
max_word_str = ''

while word != 'End of words':
    if word == 'End of words':
        break
    sum_letters_word = 0
    for i in range(0, len(word)):
        current_letter = word[i]
        current_num = ord(current_letter)
        sum_letters_word += current_num
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u' or word[0] == 'y' or word[
        0] == 'A' or word[0] == 'E' or word[0] == 'I' or word[0] == 'O' or word[0] == 'U' or word[0] == 'Y':
        sum_letters_word *= len(word)
    else:
        sum_letters_word /= len(word)
    if sum_letters_word > max_word:
        max_word_str = word
        max_word = sum_letters_word
    word = input()
print(f'The most powerful word is {max_word_str} - {max_word}')

