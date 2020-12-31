# elements = input().split()
# k = int(input())
#
# new_line = []
#
# while element in elements:
#     for i in range(1, len(elements)+1):
#         if i % 3 == 0:
#             new_line.append(elements.pop(i))
#
# print(new_line)

numbers = input().split(' ')
step = int(input())
counted = []
index = 0

while len(numbers) > 0:
    index = (index + step - 1) % len(numbers)
    counted.append(numbers.pop(index))

print(f"[{','.join(counted)}]")

