import math
series_name = input()
seasons = int(input())
episodes = int(input())
episode_time = float(input())

total_time = seasons * ((episodes - 1) * episode_time*1.2 + (episode_time*1.2 + 10))

print(f'Total time needed to watch the {series_name} series is {math.floor(total_time)} minutes.')