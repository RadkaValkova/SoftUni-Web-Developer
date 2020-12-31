number_poor_grades = int(input())
poor_grade_count = 0
is_failed = True
sum_grades = 0
count_grades = 0
last_problem = ''
while poor_grade_count < number_poor_grades:
    problem_name = input()
    if problem_name == 'Enough':
        is_failed = False
        break
    grade = int(input())
    if grade <= 4:
        poor_grade_count += 1
    sum_grades += grade
    count_grades += 1
    last_problem = problem_name
if is_failed:
    print(f'You need a break, {poor_grade_count} poor grades.')
else:
    print(f'Average score: {sum_grades/count_grades:.2f}')
    print(f'Number of problems: {count_grades}')
    print(f'Last problem: {last_problem}')

# poor_grades_max = int(input())
# poor_grade_count = 0
# grade_count = 0
# sum_grades = 0
# last_problem = ''
# while True:
#     problem_name = input()
#     if problem_name == 'Enough':
#         print(f'Average score: {sum_grades/grade_count:.2f}')
#         print(f'Number of problems: {grade_count}')
#         print(f'Last problem: {last_problem}')
#         break
#     grade = int(input())
#     grade_count += 1
#     sum_grades += grade
#     if grade <= 4:
#         poor_grade_count += 1
#         if poor_grade_count == poor_grades_max:
#             print(f'You need a break, {poor_grade_count} poor grades.')
#             break
#     last_problem = problem_name