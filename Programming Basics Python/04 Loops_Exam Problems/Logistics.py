number_of_loads = int(input())

weight_microbus = 0
weight_truck = 0
weight_train = 0

for weight in range (1,number_of_loads + 1):
    current_weight = int(input())
    if current_weight <= 3:
        weight_microbus = weight_microbus + current_weight
    elif current_weight > 3 and current_weight <= 11:
        weight_truck = weight_truck + current_weight
    else:
        weight_train = weight_train + current_weight

value_microbus = weight_microbus * 200
value_truck = weight_truck * 175
value_train = weight_train * 120
average_price = (value_microbus+value_truck+value_train) / (weight_microbus+weight_truck+weight_train)
total_weight = (weight_microbus + weight_truck + weight_train)

print(f'{average_price:.2f}')
print(f'{(weight_microbus/total_weight*100):.2f}%')
print(f'{(weight_truck/total_weight*100):.2f}%')
print(f'{(weight_train/total_weight*100):.2f}%')

