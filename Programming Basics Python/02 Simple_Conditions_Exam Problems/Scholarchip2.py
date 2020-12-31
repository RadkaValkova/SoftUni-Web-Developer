income = float(input())
grade = float(input())
salary = float(input())

excellent_scholarchip = 0
social_scholarchip = 0

if grade >= 5.50:
    excellent_scholarchip += grade * 25
if grade > 4.5 and income < salary:
    social_scholarchip += salary * 0.35

if social_scholarchip > excellent_scholarchip:
    print(f'You get a Social scholarship {social_scholarchip} BGN')
elif excellent_scholarchip >= social_scholarchip:
    if excellent_scholarchip != 0:
        print(f'You get a scholarship for excellent results {scholarship} BGN')
    else:
        print('You cannot get a scholarship!')
