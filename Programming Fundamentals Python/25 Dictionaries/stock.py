stock = input().split()
searched_product = input().split()

my_stock = {}

for i in range(0,len(stock), 2):
    product = stock[i]
    quantity = int(stock[i+1])
    my_stock[product] = quantity
    # това може и с компрехеншън my_stock = {stock[i] : int(stock[i+1]) for i in range(0,len(stock),2)}

for prod in searched_product:
    if prod in my_stock:
        print(f'We have {my_stock[prod]} of {prod} left')
    else:
        print(f'Sorry, we don\'t have {prod}')