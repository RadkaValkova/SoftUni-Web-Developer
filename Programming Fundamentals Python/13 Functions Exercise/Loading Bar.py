number = int(input())


def loading_bar(number):
    result = ('%' * (number // 10) + '.' * ((100 - number) // 10))
    final = f'{number}% [{result}]'
    if number == 100:
        return f'100% Complete!\n[{result}]'
    else:
        return f'{final}\nStill loading...'


print(loading_bar(number))
