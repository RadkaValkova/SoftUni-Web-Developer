def get_not_arrived_guests(invited_guests, arrived_guests):
    # guests_set = set(invited_guests)
    # [guests_set.remove(guest) for guest in arrived_guests]
    # return guests_set
    return set(invited_guests) - set(arrived_guests)


def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


guests_num = int(input())
invited_guests = [input() for _ in range(guests_num)]
arrived_guests = []

while True:
    line = input()
    if line == 'END':
        break
    arrived_guests.append(line)

print_result(get_not_arrived_guests(invited_guests, arrived_guests))
