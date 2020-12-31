def calculate_result(first,second):
    result = 0
    for i in range(len(first)):
        result += ord(first[i]) * ord(second[i])
    for y in range(len(first),len(second)):
        result += ord(second[y])
    return result


strings = input().split()
first = strings[0]
second = strings[1]

if len(first) <= len(second):
    print(calculate_result(first,second))
else:
    print(calculate_result(second,first))

