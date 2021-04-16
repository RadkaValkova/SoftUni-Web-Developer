from statistics import mean

students_number = int(input())

students = {}

for i in range(students_number):
    line = input().split()
    current_student = line[0]
    current_grade = float(line[1])
    if current_student not in students:
        students[current_student] = []
    students[current_student].append(current_grade)

for name, grades in students.items():
    average_grade = sum(grades)/len(grades)
    print(f'{name} -> {" ".join([f"{x:.2f}" for x in grades])} (avg: {average_grade:.2f})')