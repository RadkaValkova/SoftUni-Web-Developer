string = input()
new_list = []

my_list = string.split()
for i in range(len(my_list)):
    current_num = my_list[i]
    new_element = int(current_num) * - 1 # това може да се запише и като -int(current_num)
    new_list.append(new_element)
print(new_list)
