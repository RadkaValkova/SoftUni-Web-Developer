hour = int(input())
day = input()

if 10 <= hour <= 18:
    if day == 'Sunday':
        print('closed')
    else:
        print('open')
else:
    print('closed')