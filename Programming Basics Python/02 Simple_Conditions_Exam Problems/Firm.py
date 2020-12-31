import math
needed_hours = int(input())
working_days = int(input())
workers = int(input())

possible_project_days = working_days * 0.9
possible_project_hours = possible_project_days * (8+2) * workers
difference = math.fabs(possible_project_hours - needed_hours)

if  possible_project_hours >= needed_hours:
    print(f'Yes!{math.floor(difference)} hours left.')
else:
    print(f'Not enough time!{math.floor(difference)} hours needed.')