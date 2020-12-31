people = int(input())
wagons = list(map(int, input().split()))

max_people = len(wagons) * 4

for i in range(len(wagons)):
    for y in range(4):
        if wagons[i] < 4:
            wagons[i] += 1
            people -= 1

            if people == 0 and max_people - sum(wagons) > 0:
                print(f'The lift has empty spots!\n{" ".join(list(map(str, wagons)))}')
                break
            elif people > 0 and max_people - sum(wagons) == 0:
                print(f'There isn\'t enough space! {people} people in a queue!\n{" ".join(list(map(str, wagons)))}')
                break
            elif people == 0 and max_people - sum(wagons) == 0:
                print(" ".join(list(map(str, wagons))))
                break

# people = int(input())
# wagons = list(map(int,input().split()))
#
# for i in range(len(wagons)):
#     while wagons[i] < 4 and people > 0:
#         wagons[i] += 1
#         people -= 1
#
# if people > 0 and sum(wagons) == len(wagons)*4:
#     print(f'There isn\'t enough space! {people} people in a queue!')
# elif people <= 0 and sum(wagons) < len(wagons)*4:
#     print('The lift has empty spots!')
#
# print(' '.join(list(map(str,wagons))))