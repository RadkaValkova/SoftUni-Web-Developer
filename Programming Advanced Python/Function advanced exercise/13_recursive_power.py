def recursive_power(number,power):
    if power == 1:
        return number
    for i in range(power):
        return number * recursive_power(number, power -1)

print(recursive_power(2, 5))