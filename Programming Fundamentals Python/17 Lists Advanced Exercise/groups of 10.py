numbers = list(map(int, (input().split(', '))))

boundary = 10

while len(numbers) != 0:
    new_list = list(filter(lambda x: x <= boundary, numbers))  # [num for num in numbers if num <= boundary]
    for number in new_list:         # numbers = list(filter(lambda x: x > boundary, numbers)
        numbers.remove(number)
    print(f'Group of {boundary}\'s: {new_list}')
    boundary += 10
