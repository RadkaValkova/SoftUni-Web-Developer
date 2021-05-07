from collections import deque


def is_secondary_color(result,dic,ll):
    if dic[result][0] in ll and dic[result][1] in ll:
        return True
    else:
        return False


main_colors = ['red', 'yellow', 'blue']
secondary_colors = {'orange': ['red', 'yellow'], 'purple': ['red', 'blue'], 'green': ['yellow', 'blue']}

string = deque(input().split())
found_colors = []

while string:
    first = string[0]
    second = string[-1]
    if first == '' and second == '':
        break
    result1 = first + second
    result2 = second + first

    if result1 in main_colors or result1 in secondary_colors:
        found_colors.append(result1)
        string.popleft()
        string.pop()
    elif result2 in main_colors or result2 in secondary_colors:
        found_colors.append(result2)
        string.popleft()
        string.pop()
    else:
        first = first[:-1]
        second = second[:-1]
        string.insert(len(string)//2, first)
        string.insert(len(string)//2, second)
        string.popleft()
        string.pop()

for col in found_colors:
    if col in secondary_colors:
        range_list = secondary_colors[col]
        if range_list[0] not in found_colors or range_list[1] not in found_colors:
            found_colors.remove(col)


print(found_colors)