password = input()


def password_validation(password):
    result = []
    dig_counter = 0
    is_valid_length = len(password) >= 6 and len(password) <= 10
    only_letters_and_digits = password.isalnum()
    # has_at_last_two_digits = len([x for x in password if x.isdigit()]) >= 2
    for i in range(len(password)):
        current_char = password[i]
        if current_char.isdigit():
            dig_counter += 1
    has_two_digits = dig_counter >= 2

    if is_valid_length and only_letters_and_digits and has_two_digits:
        result.append('Password is valid')
    if not is_valid_length:
        result.append('Password must be between 6 and 10 characters')
    if not only_letters_and_digits:
        result.append('Password must consist only of letters and digits')
    if not has_two_digits:
        result.append('Password must have at least 2 digits')

    return result


print('\n'.join(password_validation(password)))

# def is_password_valid(password: str):
#     result = []
#     counter = 0
#     for i in range(len(password)):
#         if password[i].isdigit():
#             counter += 1
#     if password.isalnum() and (6 <= len(password) <= 10) and counter >= 2:
#         result.append('Password is valid')
#     else:
#         if not (6 <= len(password) <= 10):
#             result.append('Password must be between 6 and 10 characters')
#         if not password.isalnum():
#             result.append('Password must consist only of letters and digits')
#         if counter < 2:
#             result.append('Password must have at least 2 digits')
#     return result
#
#
# password = input()
# print('\n'.join(is_password_valid(password)))