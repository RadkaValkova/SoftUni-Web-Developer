def even_odd(*args):
    args_list = [x for x in args]
    command = args_list.pop()

    if command == 'even':
        return [x for x in args_list if int(x) % 2 == 0]
    else:
        return [x for x in args_list if int(x) % 2 == 1]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# def even_odd(*args):
#     if args[-1] == 'odd':
#         return [el for el in args[:len(args)-1] if el % 2 == 1]
#     else:
#         return [el for el in args[:len(args) - 1] if el % 2 == 0]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
