name = input()
years = 1
total_sum = 0
failed_counter = 0
excluded = False
while years <= 12:
    grade = float(input())
    if grade >= 4:
        years += 1
        total_sum += grade
    else:
        failed_counter += 1
        if failed_counter == 2:
            excluded = True
            break
if excluded:
    print(f'{name} has been excluded at {years} grade')
else:
    average_grade = total_sum/12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')

# name = input()
# poor_grades = 0
# class_count = 0
# sum_grades = 0
# while True:
#     grade = float(input())
#     sum_grades += grade
#     class_count += 1
#     if grade < 4:
#         poor_grades += 1
#         if poor_grades == 2:
#             class_count -= 1
#             print(f'{name} has been excluded at {class_count} grade')
#             break
#     else:
#         if class_count == 12:
#             print(f'{name} graduated. Average grade: {sum_grades / class_count:.2f}')
#             break
