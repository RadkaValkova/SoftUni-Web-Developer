width = int(input())
length = int(input())
height = int(input())

free_volume = width * length * height
boxes = input()
sum_boxes = 0
enough_space = True
while boxes != 'Done':
    sum_boxes += int(boxes)
    if free_volume < sum_boxes:
        enough_space = False
        break
    boxes = input()

if enough_space:
    print(f'{free_volume - sum_boxes} Cubic meters left.')
else:
    print(f'No more free space! You need {sum_boxes - free_volume} Cubic meters more.')

# l = int(input())
# h = int(input())
# w = int(input())
# free_space = l*h*w
# sum_boxes = 0
#
# while True:
#     boxes = input()
#     if boxes == 'Done':
#         print(f'{free_space-sum_boxes} Cubic meters left.')
#         break
#     sum_boxes += int(boxes)
#     if free_space <= sum_boxes:
#         print(f'No more free space! You need {sum_boxes-free_space} Cubic meters more.')
#         break