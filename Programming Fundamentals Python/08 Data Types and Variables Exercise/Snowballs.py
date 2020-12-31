import sys
snowballs_number = int(input())
max_result = -sys.maxsize
max_snow = 0
max_time = 0
max_quality = 0

for i in range(1, snowballs_number+1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    snowball_result = int((snow / time) ** quality)
    if snowball_result > max_result:
        max_result = snowball_result
        max_snow = snow
        max_time = time
        max_quality = quality

print(f'{max_snow} : {max_time} = {max_result} ({max_quality})')