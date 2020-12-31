visitors = int(input())
visitors_counter = 0
work_out_counter = 0
protein_counter = 0
Back_counter = 0
Chest_counter = 0
Legs_counter = 0
Abs_counter = 0
Protein_shake_counter = 0
Protein_bar_counter = 0

for i in range(1, visitors + 1):
    activity = input()
    visitors_counter += 1
    if activity == 'Back':
        work_out_counter += 1
        Back_counter += 1
    elif activity == 'Chest':
        work_out_counter += 1
        Chest_counter += 1
    elif activity == 'Legs':
        work_out_counter += 1
        Legs_counter += 1
    elif activity == 'Abs':
        work_out_counter += 1
        Abs_counter += 1

    if activity == 'Protein shake':
        protein_counter += 1
        Protein_shake_counter += 1
    elif activity == 'Protein bar':
        protein_counter += 1
        Protein_bar_counter += 1

print(f'{Back_counter} - back')
print(f'{Chest_counter} - chest')
print(f'{Legs_counter} - legs')
print(f'{Abs_counter} - abs')
print(f'{Protein_shake_counter} - protein shake')
print(f'{Protein_bar_counter} - protein bar')
print(f'{(work_out_counter/visitors_counter*100):.2f}% - work out')
print(f'{((protein_counter/visitors_counter)*100):.2f}% - protein')
