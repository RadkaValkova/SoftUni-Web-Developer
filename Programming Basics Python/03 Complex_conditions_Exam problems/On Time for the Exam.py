exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
student_arrival = 0
result = 0
hours = 0
minutes = 0

exam_time = exam_hour*60 + exam_minutes
arrival_time = arrival_hour*60 + arrival_minutes
difference = arrival_time - exam_time

if exam_time < arrival_time:
    student_arrival = 'Late'
elif exam_time == arrival_time or (exam_time-30) <= arrival_time:
    student_arrival = 'On time'
else:
    student_arrival = 'Early'

if difference != 0:
    hours = abs(difference) // 60
    minutes = abs(difference) % 60
    if hours > 0:
        result = (f'{hours}:{minutes:02} hours')
    else:
        result = (f'{minutes} minutes')
    if difference < 0:
        result += ' before the start'
    else:
        result += ' after the start'
print(student_arrival)
print(result)