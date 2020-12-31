n = int(input())

strings_list = []
balanced = []

for element in range(n):
    current_element = input()
    if current_element == '(' or current_element == ')':
        strings_list.append(current_element)

for i in range(len(strings_list)):
    if strings_list[i] == '(' and strings_list[i+1] == ')':
        balanced.append(0)

if len(balanced) == len(strings_list) / 2:
    print('BALANCED')
else:
    print('UNBALANCED')


