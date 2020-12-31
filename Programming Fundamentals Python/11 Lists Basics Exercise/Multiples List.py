factor = int(input())
count = int(input())
start_element = 1
divided_elements = []

while len(divided_elements) < count:
    if start_element % factor == 0:
        divided_elements.append(start_element)
    start_element += 1
print(divided_elements)

