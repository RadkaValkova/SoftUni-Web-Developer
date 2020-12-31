def sum_odd_and_even_digits(num):
    sum_odd = 0
    sum_even = 0
    for dig in num:
        dig = int(dig)
        if dig % 2 != 0:
            sum_odd += int(dig)
        elif dig % 2 == 0:
            sum_even += int(dig)
    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


number = input()
print(sum_odd_and_even_digits(number))

# number = input()
#
#
# def odd_and_even_sum_of_the_digits(number):
#     digit_list = []
#     for y in range(len(number)):
#         current_num = number[y]
#         digit_list.append(current_num)
#     odd_digits = []
#     even_digits = []
#     for i in range(len(digit_list)):
#         current_digit = int(digit_list[i])
#         if current_digit != 0:
#             if current_digit % 2 == 0:
#                 even_digits.append(current_digit)
#             else:
#                 odd_digits.append(current_digit)
#     return f'Odd sum = {sum(odd_digits)}, Even sum = {sum(even_digits)}'
#
#
# print(odd_and_even_sum_of_the_digits(number))
