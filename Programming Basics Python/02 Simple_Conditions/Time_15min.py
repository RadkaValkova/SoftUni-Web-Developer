hours = int(input())
minutes = int(input())

time_in_minutes = hours*60 + minutes +15
hours = time_in_minutes // 60
minutes = time_in_minutes % 60

if hours <= 23:
    hours = hours
else:
    hours = hours % 23 -1

if minutes < 10:
    minutes = f'0{minutes}'
else:
    minutes = minutes

print(f'{hours}:{minutes}')

