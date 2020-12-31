# list_of_integers = input().split()
#
#
# def is_palindrome(list_of_integers):
#     for i in range(len(list_of_integers)):
#         element = list_of_integers[i]
#         forward = element[:]
#         backward = element[::-1]
#         if forward == backward:
#             print('True')
#         else:
#             print('False')
#
#
# is_palindrome(list_of_integers)

def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False


numbers = input().split(', ')

for num in numbers:
    print(is_palindrome(num))