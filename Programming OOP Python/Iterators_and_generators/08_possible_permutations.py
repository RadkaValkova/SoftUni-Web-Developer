from itertools import permutations


def possible_permutations(ll):
    for perm in permutations(ll):
        yield list(perm)

[print(n) for n in possible_permutations([1, 2, 3])]