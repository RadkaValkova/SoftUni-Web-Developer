begin_number = int(input())
end_number = int(input())

for i in range(begin_number, end_number+1):
    for j in range(begin_number, end_number+1):
        for y in range(begin_number, end_number+1):
            for z in range(begin_number, end_number+1):
                if (i % 2 == 0 and z % 2 != 0) or ( i % 2 != 0 and z % 2 == 0):
                    if i > z:
                        if (j + y) % 2 == 0:
                            print(f'{i}{j}{y}{z}', end=' ')
