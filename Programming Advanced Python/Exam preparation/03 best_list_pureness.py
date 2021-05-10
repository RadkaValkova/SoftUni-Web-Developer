def best_list_pureness(numbers,k):
    max_pureness = 0
    max_index = 0
    for i in range(k+1):
        result = 0
        for j in range(len(numbers)):
            result += numbers[j]*j
            if result > max_pureness:
                max_pureness = result
                max_index = i
        last_num = numbers.pop()
        numbers.insert(0, last_num)
    return f'Best pureness {max_pureness} after {max_index} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

#
#
#
# def best_list_pureness(ll,k):
#     from collections import deque
#     ll = deque(ll)
#     max_pureness = 0
#     max_rotation = 0
#     for i in range(0, k+1):
#         current_pureness = sum([ll[j] * j for j in range(len(ll))])
#         if current_pureness > max_pureness:
#             max_pureness = current_pureness
#             max_rotation = i
#         ll.appendleft(ll.pop())
#     return f'Best pureness {max_pureness} after {max_rotation} rotations'
#
#
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)



