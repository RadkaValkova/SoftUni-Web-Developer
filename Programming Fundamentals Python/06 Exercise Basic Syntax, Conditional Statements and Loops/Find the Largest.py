number = input()

number_list = sorted(int(x) for x in number)
str_list = [str(x) for x in number_list]

print(''.join(reversed(str_list)))
