exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

total_exam_minutes = exam_hour * 60 + exam_minutes
total_arrival_minutes = arrival_hour * 60 + arrival_minutes
difference = total_exam_minutes - total_arrival_minutes
result = 0

if total_exam_minutes < total_arrival_minutes:
    print('Late')
elif total_exam_minutes == total_arrival_minutes or total_exam_minutes -30 <= total_arrival_minutes:
    print('On time')
else:
    print('Early')

if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    if hours > 0:
        result = (f'{hours}:{minutes:02d} hours')
    else:
        result = (f'{minutes} minutes')
    if difference > 0:
        result += ' before the start'
    else:
        result += ' after the start'
    print(result)


