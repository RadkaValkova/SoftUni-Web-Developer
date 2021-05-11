from collections import deque


def stock_availability(ll,com,*args):
    cupcake_list = ll
    command = com
    other = list(args)
    if command == 'delivery':
        cupcake_list = cupcake_list + [el for el in args]
    elif command == 'sell':
        cupcake_list = deque(cupcake_list)
        if not other:
            cupcake_list.popleft()
        elif type(other[0]) == int:
            for i in range(other[0]):
                cupcake_list.popleft()
        else:
            for el in other:
                if el in cupcake_list:
                    while el in cupcake_list:
                        cupcake_list.remove(el)

    return list(cupcake_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
