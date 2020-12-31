students_number = int(input())

excellent_number = 0
very_good_number = 0
good_number = 0
failed_number = 0
sum_grades = 0

for i in range(1,students_number + 1):
    grade = float(input())
    if grade < 3:
        sum_grades += grade
        failed_number += 1
    elif grade < 4:
        sum_grades += grade
        good_number += 1
    elif grade < 5:
        sum_grades += grade
        very_good_number += 1
    else:
        sum_grades += grade
        excellent_number +=1

average_grade = sum_grades/students_number
print(f'Top students: {excellent_number/students_number*100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good_number/students_number*100:.2f}%')
print(f'Between 3.00 and 3.99: {good_number/students_number*100:.2f}%')
print(f'Fail: {failed_number/students_number*100:.2f}%')
print(f'Average: {average_grade:.2f}')
