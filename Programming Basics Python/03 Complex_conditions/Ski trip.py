days = int(input())
room_type = input()
grade = input()

stay_value = 0
if days < 10:
    if room_type == 'room for one person':
        stay_value = (days-1)*18
    elif room_type == 'apartment':
        stay_value = (days-1)*25*0.7
    elif room_type == 'president apartment':
        stay_value = (days-1)*35*0.9
elif days >=10 and days <=15:
    if room_type == 'room for one person':
        stay_value = (days-1)*18
    elif room_type == 'apartment':
        stay_value = (days-1)*25*0.65
    elif room_type == 'president apartment':
        stay_value = (days-1)*35*0.85
elif days > 15:
    if room_type == 'room for one person':
        stay_value = (days-1)*18
    elif room_type == 'apartment':
        stay_value = (days-1)*25*0.5
    elif room_type == 'president apartment':
        stay_value = (days-1)*35*0.8

if grade == 'positive':
    stay_value = stay_value + stay_value*0.25
elif grade == 'negative':
    stay_value = stay_value - stay_value*0.1

print(f'{stay_value:.2f}')



