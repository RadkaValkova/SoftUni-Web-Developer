jury = int(input())
total_grades_sum = 0
total_counter = 0

while True:
    presentation_name = input()
    if presentation_name == 'Finish':
        print(f'Student\'s final assessment is {total_grades_sum/total_counter:.2f}.')
        break
    grade_counter = 0
    sum_grades = 0
    for i in range(1, jury + 1):
        grade = float(input())
        grade_counter += 1
        sum_grades += grade
    print(f'{presentation_name} - {sum_grades/grade_counter:.2f}.')
    total_grades_sum += sum_grades
    total_counter += grade_counter
