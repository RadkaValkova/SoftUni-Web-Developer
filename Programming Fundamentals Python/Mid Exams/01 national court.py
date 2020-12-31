first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
total_people = int(input())

mutual_capacity = first_employee_capacity + second_employee_capacity + third_employee_capacity
work_hours = 0
stay_hours = 0


while total_people > 0:
    total_people -= mutual_capacity
    work_hours += 1
    if work_hours % 4 == 0:
        work_hours += 1

print(f'Time needed: {work_hours + stay_hours}h.')

# while total_people > 0:
#     total_people -= mutual_capacity
#     work_hours += 1
#     if work_hours % 3 == 0 and total_people > 0:
#         stay_hours += 1
#
# print(f'Time needed: {work_hours + stay_hours}h.')