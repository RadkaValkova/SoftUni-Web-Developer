n = int(input())
num_list = []

for i in range(n):
    current_num = int(input())
    num_list.append(current_num)

command = input()
filtered_list = []
for current_num in num_list:
    if command == 'even' and current_num % 2 == 0:
        filtered_list.append(current_num)
    if command == 'odd' and current_num % 2 != 0:
        filtered_list.append(current_num)
    if command == 'negative' and current_num < 0:
        filtered_list.append(current_num)
    if command == 'positive' and current_num >= 0:
        filtered_list.append(current_num)
print(filtered_list)


