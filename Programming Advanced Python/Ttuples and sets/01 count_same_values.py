#
# numbers_list = [float(x) for x in input().split()]
#
# numbers_dict = {}
#
# for el in numbers_list:
#     if el not in numbers_dict:
#         numbers_dict[el] = numbers_list.count(el)
#
# for key, value in numbers_dict.items():
#     print(f'{key} - {value} times')

def count_numbers(numbers):
    num_dict = {}
    for number in numbers:
        counter = numbers.count(number)
        if number not in num_dict:
            num_dict[number] = counter
    return num_dict


def print_result(num_dict):
    for key,value in num_dict.items():
        print(f'{key} - {value} times')


numbers = list(map(float,input().split()))
print_result(count_numbers(numbers))
