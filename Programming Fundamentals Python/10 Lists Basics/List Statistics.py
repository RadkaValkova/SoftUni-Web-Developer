n = int(input())
list_positive = []
list_negative = []
positive_counter = 0
sum_negative = 0                # може да се замени както долу е отпечатано със len и sum

for i in range(n):
    current_num = int(input())
    if current_num >= 0:
        positive_counter += 1
        list_positive.append(current_num)
    else:
        list_negative.append(current_num)
        sum_negative += current_num
print(list_positive)
print(list_negative)
print(f'Count of positives: {positive_counter}. Sum of negatives: {sum_negative}')
# print (f'Count of positives: {len(list_positive)}. Sum of negatives: {sum(list_negative)}'

