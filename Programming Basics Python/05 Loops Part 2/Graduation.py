name = input()
years = 1
total_sum = 0

while years <= 12:
    grade = float(input())
    if grade >= 4:
        years += 1
        total_sum += grade

average_grade = total_sum/12
print(f'{name} graduated. Average grade: {average_grade:.2f}')



