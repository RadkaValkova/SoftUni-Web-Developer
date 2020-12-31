incomes_str = input().split(', ')
number_of_beggars = int(input())
incomes_num = []
for incomes in incomes_str:
    incomes_num.append(int(incomes))
beggars = []
for i in range(number_of_beggars):  #това същото може да стане с beggars = [0]* number_of_beggars
    beggars.append(0)

index = 0
for incomes in incomes_num:
    beggars[index] += incomes
    index += 1                               #вариант 1
    if index == number_of_beggars:
        index = 0
print(beggars)

# for i in range(len(incomes_num)):
#     element = incomes_num[i]
#     beggar_index = i % number_of_beggars    #вариант 2
#     beggars[beggar_index] += element

# numbers = input().split(', ')
# beggars_count = int(input())
#
# beggars_list = [0 for beggar in range(beggars_count)]
#
# for _ in range(len(numbers)):
#     for index in range(beggars_count):
#         if numbers:
#             beggars_list[index] += int(numbers.pop(0))
#
# print(beggars_list)
