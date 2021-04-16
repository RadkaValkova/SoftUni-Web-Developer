names_number = int(input())

unique_names = set()

for _ in range(names_number):
    name = input()
    unique_names.add(name)

for el in unique_names:
    print(el)