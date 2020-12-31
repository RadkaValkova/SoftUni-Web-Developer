n = int(input())
word = input()
my_list = []
new_list = []

for i in range(n):
    current_string = input()
    my_list.append(current_string)
    if word in current_string:
        new_list.append(current_string)

print(my_list)
print(new_list)
