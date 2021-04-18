def get_unique_elements(n):
    ss1 = set()
    for _ in range(n):
        line = input()
        [ss1.add(el) for el in line.split()]
    return ss1


def print_results(result):
    for el in result:
        print(el)


n = int(input())
print_results(get_unique_elements(n))