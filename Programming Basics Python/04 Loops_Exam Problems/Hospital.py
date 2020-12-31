days = int(input())

treated_patients = 0
untreated_patients = 0
doctors = 7

for num in range (1, days+1):
    patients_for_the_day = int(input())
    if num % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
        if doctors >= patients_for_the_day:
            treated_patients += patients_for_the_day
        else:
            treated_patients += doctors
        if doctors < patients_for_the_day:
            untreated_patients += patients_for_the_day - doctors
        else:
            untreated_patients += 0
    else:
        if doctors >= patients_for_the_day:
            treated_patients += patients_for_the_day
        else:
            treated_patients += doctors
        if doctors < patients_for_the_day:
            untreated_patients += patients_for_the_day - doctors
        else:
            untreated_patients += 0

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
