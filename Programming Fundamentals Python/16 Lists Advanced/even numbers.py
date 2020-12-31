def is_even(number):
    return number % 2 == 0


numbers = input().split(', ')
list_of_indexes = [i for i in range(len(numbers)) if is_even(int(numbers[i]))]
print(list_of_indexes)

# numbers = map(int, input().split(', '))
# indexes_list = [index for index, number in enumerate(numbers) if number % 2 == 0]
# print(indexes_list)


# string_of_numbers = input().split(', ')
#
# numbers = [int(num) for num in string_of_numbers]
# index_list = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
#
# print(index_list)