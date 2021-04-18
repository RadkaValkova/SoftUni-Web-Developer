def get_unique_names(names):
    names_set = set(names)
    return names_set


def print_result(result):
    [print(el) for el in get_unique_names(names)]


n = int(input())
names = [input() for _ in range(n)]

print_result(names)