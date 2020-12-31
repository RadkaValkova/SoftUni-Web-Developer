number_of_lines = int(input())
sum_letter_value = 0

for letter in range(number_of_lines):
    current_letter = input()
    current_letter_value = ord(current_letter)
    sum_letter_value += current_letter_value
print(f'The sum equals: {sum_letter_value}')