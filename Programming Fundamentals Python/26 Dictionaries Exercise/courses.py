course_info = {}
while True:
    line = input()
    if line == 'end':
        break
    course_name, student_name = line.split(' : ')
    if course_name not in course_info:
        course_info[course_name] = []
    course_info[course_name].append(student_name)

for key, value in sorted(course_info.items(), key=lambda x: -len(x[1])):
    print(f'{key}: {len(value)}')
    for el in sorted(course_info[key]):
        print(f'-- {el}')

