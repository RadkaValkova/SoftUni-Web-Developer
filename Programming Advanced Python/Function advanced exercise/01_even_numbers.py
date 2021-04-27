numbers = [int(x) for x in input().split()]

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)