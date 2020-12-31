numbers = input().split(', ')

zero_list = []
other_list = []

for i in range(len(numbers)):
    current_num = int(numbers[i])
    if current_num == 0:
        zero_list.append(current_num)
    else:
        other_list.append(current_num)

print(other_list + zero_list)
