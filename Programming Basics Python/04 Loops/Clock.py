hours = 23
minutes = 59
total_minutes = hours*60 + minutes

for i in range(0,total_minutes+1):
     current_hour = i // 60
     current_minutes = i % 60
     print(f'{current_hour} : {current_minutes}')

#for hour in range(0,23+1):
    #current_hour = hour
    #for minute in range(0,59+1):
        #current_minute = minute
        #print(f'{current_hour} : {current_minute}')
