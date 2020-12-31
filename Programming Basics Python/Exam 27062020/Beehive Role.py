intelekt = int(input())
power = int(input())
sex = input()
role = ''

if intelekt >= 80 and power >= 80 and sex == 'female':
    role = 'Queen Bee'
elif intelekt >= 80:
    role = 'Repairing Bee'
elif intelekt >= 60:
    role = 'Cleaning Bee'
elif power >= 80 and sex == 'male':
    role = 'Drone Bee'
elif power >= 60:
    role = 'Guard Bee'
else:
    role = 'Worker Bee'

print(role)

