def odd_or_even(command, numbers):
    if command == 'Odd':
        return sum([x for x in numbers if x % 2 == 1]) * len(numbers)
    else:
        return sum([x for x in numbers if x % 2 == 0]) * len(numbers)


command = input()
numbers = [int(x) for x in input().split()]

print(odd_or_even(command,numbers))