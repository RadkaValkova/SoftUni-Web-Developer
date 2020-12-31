import math
series_name = input()
episode_time = int(input())
break_time = int(input())

lunch = break_time * 1/8
rest = break_time * 1/4
time_for_watch = break_time - lunch - rest

if time_for_watch >= episode_time:
    print(f'You have enough time to watch {series_name} and left with {math.ceil(time_for_watch-episode_time)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {series_name}, you need {math.ceil(episode_time - time_for_watch)} more minutes.')