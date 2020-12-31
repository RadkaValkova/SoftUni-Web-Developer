import sys
numbers = input().split()
num_to_remove = int(input())

for y in range(num_to_remove):
    min_number = sys.maxsize
    for i in range(len(numbers)):
        current_number = int(numbers[i])
        if current_number < min_number:
            min_number = current_number
    numbers.remove(str(min_number))
numbers = list(map(int, numbers))
print(numbers)

# numbers = input().split()
# n = int(input())
#
# int_list = []
# for i in range(len(numbers)):
#     number = int(numbers[i])
#     int_list.append(number)
#
# for y in range(n):
#     current_num = min(int_list)
#     int_list.remove(current_num)
# print(int_list)
