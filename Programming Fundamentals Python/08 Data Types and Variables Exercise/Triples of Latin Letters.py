n = int(input())

for i in range(97, 97+n):
    current_i = chr(i)
    for y in range(97, 97+n):
        current_y = chr(y)
        for z in range(97, 97+n):
            current_z = chr(z)
            print(f'{current_i}{current_y}{current_z}')