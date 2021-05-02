file_path = '/13_file_handling\Files/File Reader/numbers.txt'

# file = open(file_path, 'r')

# lines = file.readlines()
#
# print(sum(int(num) for num in lines))


def calculate_sum_with_loop(file_path):
    file = open(file_path, 'r')
    result = 0
    for el in file:
        result += int(el)
    return result


def calculate_sum_with_readline(file_path):
    file = open(file_path, 'r')
    result = 0
    while True:
        number_str = file.readline()
        if not number_str:
            break
        result += int(number_str)
    return result


print(calculate_sum_with_loop(file_path))
print(calculate_sum_with_readline(file_path))