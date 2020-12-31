first_student_capacity = int(input())
second_student_capacity = int(input())
third_student_capacity = int(input())
total_people = int(input())

mutual_capacity = first_student_capacity + second_student_capacity + third_student_capacity
work_hours = 0
stay_hours = 0


while total_people > 0:
    total_people -= mutual_capacity
    work_hours += 1
    if work_hours % 3 == 0 and total_people > 0:
        stay_hours += 1

print(f'Time needed: {work_hours + stay_hours}h.')