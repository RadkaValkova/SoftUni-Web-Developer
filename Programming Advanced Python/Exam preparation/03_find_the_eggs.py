def find_strongest_eggs(*args):
    ll = args[0]
    num = args[1]
    sub_lists = []
    for r in range(num):
        row = []
        for j in range(r,len(ll), num):
            row.append(ll[j])
        sub_lists.append(row)

    max_eggs_list = []
    for i in range(num):
        current_row = sub_lists[i]
        middle_index = len(current_row)//2
        mid_element = current_row[middle_index]
        max_element = max([el for el in range(middle_index, len(current_row))])
        if mid_element > max_element:
            max_eggs_list.append(mid_element)
    return max_eggs_list


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))



