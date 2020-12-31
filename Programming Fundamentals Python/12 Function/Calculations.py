operator = input()
num_1 = int(input())
num_2 = int(input())


# def calculate_result():
#     if operator == 'multiply':
#         return num_1 * num_2
#     if operator == 'divide':
#         return num_1 / num_2
#     if operator == 'add':
#         return num_1 + num_2
#     if operator == 'subtract':
#         return num_1 - num_2
#
#
# print(int(calculate_result()))
def calculate_result(a,b, operation):
    result = None
    if operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        result = a / b
    elif operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    return result


print(calculate_result(num_1, num_2, operator))
