line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

winner = ''

if line_1[0] == line_2[0] == line_3[0]:
    winner = line_1[0]
elif line_1[1] == line_2[1] == line_3[1]:
    winner = line_1[1]
elif line_1[2] == line_2[2] == line_3[2]:
    winner = line_1[2]
elif line_1[0] == line_1[1] == line_1[2]:
    winner = line_1[0]
elif line_2[0] == line_2[1] == line_2[2]:
    winner = line_2[0]
elif line_3[0] == line_3[1] == line_3[2]:
    winner = line_3[0]
elif line_1[0] == line_2[1] == line_3[2]:
    winner = line_1[0]
elif line_1[2] == line_2[1] == line_3[0]:
    winner = line_1[2]

if winner == '1':
    print(f'First player won')
elif winner == '2':
    print(f'Second player won')
else:
    print(f'Draw!')