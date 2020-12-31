import math

record_sec = float(input())
distance_m = float(input())
ivan_sec_for_m = float(input())

ivan_time = distance_m * ivan_sec_for_m
delay_for_distance = distance_m // 15 * 12.5
total_time_ivan = (ivan_time + delay_for_distance)

if total_time_ivan < record_sec:
    print(f'Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time_ivan - record_sec:.2f} seconds slower.')