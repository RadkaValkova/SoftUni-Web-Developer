elements = input().lower().split()

elements_dict = {}

for element in elements:
    if element not in elements_dict:
        elements_dict[element] = 0
    elements_dict[element] += 1

odd_elements = [key for (key, value) in elements_dict.items() if value % 2 != 0]
#
# for (key, value) in elements_dict.items():
#     if value % 2 != 0:
#         odd_elements.append(key)

print(' '.join(odd_elements))
