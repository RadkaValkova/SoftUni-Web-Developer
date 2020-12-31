actor_name = input()
academy_points = float(input())
jury_number = int(input())
result = academy_points

for i in range(1,jury_number+1):
    jury_name = input()
    jury_points = float(input())
    if result > 1250.5:
        break
    result += (len(jury_name) * jury_points) / 2

if result > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {result:.1f}!')
else:
    print(f'Sorry, {actor_name} you need {(1250.5-result):.1f} more!')