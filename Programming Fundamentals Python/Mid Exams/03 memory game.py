elements = input().split()

moves_until_now = 0
while True:
    line = input()
    if line == 'end':
        if len(elements) > 0:
            print(f'Sorry you lose :(\n{" ".join(elements)}')
        break
    idx_1 = int(line.split()[0])
    idx_2 = int(line.split()[1])
    moves_until_now += 1

    if idx_1 == idx_2 or (idx_1 not in range(len(elements)) or idx_2 not in range(len(elements))):
        first_half = elements[:(len(elements)//2)]
        second_half = elements[(len(elements)//2):]
        new_element = f'-{moves_until_now}a'
        elements = first_half + [new_element] + [new_element] + second_half
        print('Invalid input! Adding additional elements to the board')
    else:
        if elements[idx_1] != elements[idx_2]:
            print('Try again!')
        else:
            print(f'Congrats! You have found matching elements - {elements[idx_1]}!')
            if idx_1 > idx_2:
                elements.pop(idx_1)
                elements.pop(idx_2)
            else:
                elements.pop(idx_2)
                elements.pop(idx_1)
            if len(elements) == 0:
                print(f'You have won in {moves_until_now} turns!')
                break

def valid_index(a,b,elements):
    if a != b and a in range(len(elements)) and b in range(len(elements)):
        return True


# elements = input().split()
# movies_counter = 0
# line = input()
#
# while line != 'end':
#     idx1 = int(line.split()[0])
#     idx2 = int(line.split()[1])
#
#     movies_counter += 1
#     if not valid_index(idx1,idx2,elements):
#         print('Invalid input! Adding additional elements to the board')
#         middle_elements = len(elements) // 2
#         new_element = f'-{movies_counter}a'
#         elements.insert(middle_elements, new_element)
#         elements.insert(middle_elements, new_element)
#     else:
#         if elements[idx1] == elements[idx2]:
#             print(f'Congrats! You have found matching elements - {elements[idx1]}!')
#             matching_element = elements[idx1]
#             elements.remove(matching_element)
#             elements.remove(matching_element)
#
#         elif elements[idx1] != elements[idx2]:
#             print('Try again!')
#     if len(elements) == 0:
#         print(f'You have won in {movies_counter} turns!')
#         break
#     line = input()
#
# if len(elements) > 0:
#     print('Sorry you lose :(')
#     print(' '.join(elements))
