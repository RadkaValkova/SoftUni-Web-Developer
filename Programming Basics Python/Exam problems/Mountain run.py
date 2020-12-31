import math
record_sek = float(input())
distans_m = float(input())
time_for_m = float(input())

time_for_distans_sek = distans_m * time_for_m
slow_down_for_distance = (math.floor(distans_m/50))*30
Georgi_time = time_for_distans_sek+slow_down_for_distance

if record_sek > Georgi_time:
    print(f'Yes! The new record is {(Georgi_time):.2f} seconds.')
else:
    print(f'No! He was {(Georgi_time-record_sek):.2f} seconds slower.')