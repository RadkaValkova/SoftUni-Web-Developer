n = int(input())

students_dict = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

average_grade_dict = {}
for key,value in students_dict.items():
    average = sum(value)/len(value)
    if average >= 4.50:
        average_grade_dict[key] = average

for key,value in sorted(average_grade_dict.items(), key= lambda x: x[1], reverse=True):
    print(f'{key} -> {value:.2f}')
