words = input().split()

for word in words:
    new_word = ''
    first_letter = chr(int(''.join(ch for ch in word if ch.isdigit())))
    left_letters = [ch for ch in word if ch.isalpha()]
    left_letters[0], left_letters[-1] = left_letters[-1], left_letters[0]

    new_word += first_letter
    new_word += ''.join(left_letters)

    print(new_word, end=' ')
