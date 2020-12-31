rests_days = int(input())
work_days = 365-rests_days
minutes_in_year = work_days * 63 + rests_days * 127

if minutes_in_year >= 30000:
    print('Tom will run away')
    print(f'{(minutes_in_year - 30000) // 60} hours and {(minutes_in_year - 30000)% 60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{(30000 - minutes_in_year) // 60} hours and {(30000 - minutes_in_year) % 60} minutes less for play')
