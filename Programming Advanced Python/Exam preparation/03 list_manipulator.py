def list_manipulator(ll,*args):
    numbers_list = ll
    second, third, *others = args
    if second == 'add':
        if third == 'beginning':
            numbers_list = others + numbers_list
            return numbers_list
        elif third == 'end':
            numbers_list = numbers_list + others
            return numbers_list

    elif second == 'remove':
        if third == 'beginning':
            if others:
                for i in range(others[0]):
                    ll.pop(0)
            else:
                ll.pop(0)
            return ll
        elif third == 'end':
            if others:
                for i in range(others[0]):
                    ll.pop()
            else:
                ll.pop()
            return ll



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

# from collections import deque
#
#
# def list_manipulator(first,second,third,*args):
#     numbers = deque(first)
#
#     if second == 'add':
#         numbers = list(numbers)
#         if third == 'beginning':
#             numbers = list(args) + list(numbers)
#         elif third == 'end':
#             numbers = list(numbers) + list(args)
#
#     elif second == 'remove':
#         if third == 'beginning':
#             if args:
#                 for i in range(*args):
#                     numbers.popleft()
#             else:
#                 numbers.popleft()
#         elif third == 'end':
#             if args:
#                 for i in range(*args):
#                     numbers.pop()
#             else:
#                 numbers.pop()
#     return list(numbers)