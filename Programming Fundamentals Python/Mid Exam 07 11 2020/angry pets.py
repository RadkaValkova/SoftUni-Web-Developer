def sum_elements(my_list, type_of_items, type_of_price):
    for i in range(len(my_list)):
        if type_of_items == 'cheap':
            my_list = [el for el in my_list if el < entry_point_value]
        else:
            my_list = [el for el in my_list if el >= entry_point_value]
        if type_of_price == 'positive':
            my_list = [el for el in my_list if el > 0]
        elif type_of_price == 'negative':
            my_list = [el for el in my_list if el < 0]
        else:
            my_list = my_list
        return sum(my_list)


price_rating = list(map(int,input().split()))
entry_point_index = int(input())
type_of_items = input()
type_of_price = input()

left = [price_rating[i] for i in range(0, entry_point_index)]
right = [price_rating[i] for i in range(entry_point_index, len(price_rating))]
entry_point_value = price_rating[entry_point_index]

left_sum = sum_elements(left,type_of_items,type_of_price)
right_sum = sum_elements(right,type_of_items,type_of_price)

if left_sum >= right_sum:
    print(f'Left – {left_sum}')
else:
    print(f'Right - {right_sum}')