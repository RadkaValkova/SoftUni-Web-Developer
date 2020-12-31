budget = float(input())
flour_price = float(input())

pack_of_eggs = flour_price * 0.75
milk_price = flour_price *1.25
one_cozonac = pack_of_eggs + flour_price + milk_price *0.25

cozonak_counter = 0
eggs_counter = 0

while budget > one_cozonac:
    budget -= one_cozonac
    cozonak_counter += 1
    eggs_counter += 3
    if cozonak_counter % 3 == 0:
        eggs_counter -= (cozonak_counter - 2)

print(f'You made {cozonak_counter} cozonacs! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.')