employees = {}

while True:
    line = input()
    if line == 'End':
        break
    company_name = line.split(' -> ')[0]
    id_number = line.split(' -> ')[1]
    if company_name not in employees:
        employees[company_name] = []
    if id_number not in employees[company_name]:
        employees[company_name].append(id_number)

for key,value in sorted(employees.items(), key= lambda x: x[0]):
    print(f'{key}')
    for i in range(len(value)):
        print(f'-- {value[i]}')