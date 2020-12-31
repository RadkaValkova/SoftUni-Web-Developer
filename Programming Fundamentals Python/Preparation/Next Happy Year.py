current_year = int(input())
next_happy_year = current_year
while True:
    a = str(next_happy_year)[0]
    b = str(next_happy_year)[1]
    c = str(next_happy_year)[2]
    d = str(next_happy_year)[3]
    if a != b and a != c and a != d and b != c and b != d and c != d:
        next_happy_year = (f'{a}{b}{c}{d}')
        print(next_happy_year)
        break
    next_happy_year = int(f'{a}{b}{c}{d}') + 1
