mans = int(input())
women = int(input())
tables = int(input())

counter = 0

for man in range(1, mans+1):
    for wom in range(1, women+1):
        counter += 1
        if tables >= counter:
            print(f'({man} <-> {wom})', end=' ')
        else:
            break
