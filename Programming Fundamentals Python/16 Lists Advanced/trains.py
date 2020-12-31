wagons = int(input())

wagons_list = [0] * wagons

while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'add':
        wagons_list[-1] += int(command[1])
    elif command[0] == 'insert':
        idx = int(command[1])
        wagons_list[idx] += int(command[2])
    elif command[0] == 'leave':
        idx = int(command[1])
        wagons_list[idx] -= int(command[2])

print(wagons_list)