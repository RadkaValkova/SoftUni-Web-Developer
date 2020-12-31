control_min = int(input())
control_sek = int(input())
distance_m = float(input())
marin_sec_for_100m = int(input())

total_control_sek = control_min*60 + control_sek

marin_time = distance_m/100 * marin_sec_for_100m
delay_for_distance = distance_m / 120 * 2.5
total_time_marin = (marin_time - delay_for_distance)

if total_time_marin <= total_control_sek:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {total_time_marin:.3f}.')
else:
    print(f'No, Marin failed! He was {total_time_marin-total_control_sek:.3f} second slower.')