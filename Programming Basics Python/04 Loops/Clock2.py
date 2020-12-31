hours = 23
minutes = 59
sec = 59
total_sec = hours*3600 + minutes*60 + sec

for i in range(0,total_sec+1):
     current_hour = i // 3600
     current_minutes = i // 60 - current_hour*60
     current_sec = i % 60
     print(f'{current_hour} : {current_minutes} : {current_sec}')