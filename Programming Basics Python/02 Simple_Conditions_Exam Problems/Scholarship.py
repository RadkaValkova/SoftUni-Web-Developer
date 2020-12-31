import math
income = float(input())
success_aver = float(input())
minimal_selary = float(input())

scholarship = 0

social_scholarship = math.floor(minimal_selary * 0.35)
susccess_scholarship = math.floor(success_aver * 25)

sotial_scholarship_aprooved = income < minimal_selary and success_aver > 4.50 and success_aver < 5.50
success_scholarship_aprooved = success_aver >= 5.50

if not success_scholarship_aprooved and not sotial_scholarship_aprooved:
    print('You cannot get a scholarship!')
elif income < minimal_selary and success_scholarship_aprooved:
    if social_scholarship > susccess_scholarship:
        scholarship = social_scholarship
        print(f'You get a Social scholarship {scholarship} BGN')
    elif susccess_scholarship > social_scholarship:
        scholarship = susccess_scholarship
        print(f'You get a scholarship for excellent results {scholarship} BGN')
    else:
        scholarship = susccess_scholarship
        print(f'You get a scholarship for excellent results {scholarship} BGN')
elif sotial_scholarship_aprooved:
    scholarship = social_scholarship
    print(f'You get a Social scholarship {scholarship} BGN')
elif success_scholarship_aprooved:
    scholarship = susccess_scholarship
    print(f'You get a scholarship for excellent results {scholarship} BGN')
