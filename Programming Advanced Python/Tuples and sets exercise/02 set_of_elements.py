def unique_elements(ss1, ss2):
    result = ss1.intersection(ss2)
    return result


def print_result(result):
    for el in result:
        print(el)


line = input().split()
n = int(line[0])
m = int(line[1])

first_set = set([input() for _ in range(n)])
second_set = set([input() for _ in range(m)])

print_result(unique_elements(first_set,second_set))
