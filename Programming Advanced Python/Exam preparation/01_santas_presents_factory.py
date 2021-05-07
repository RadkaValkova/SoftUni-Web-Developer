from collections import deque

materials = [int(el) for el in input().split()]
magics = deque([int(el) for el in input().split()])
boxes_values = {150:'Doll', 250:'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
made_boxes = {'Doll':0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
succseed_boxes = False

while True:
    if not materials:
        break
    if not magics:
        break
    first_magic = magics[0]
    last_material = materials[-1]
    if first_magic * last_material in boxes_values:
        made_boxes[boxes_values[first_magic * last_material]] += 1
        magics.popleft()
        materials.pop()
    else:
        value = first_magic * last_material
        if first_magic * last_material > 0:
            magics.popleft()
            materials[-1] += 15
        elif first_magic * last_material < 0:
            materials.append(magics.popleft()+materials.pop())
        else:
            if first_magic == 0:
                magics.popleft()
            if last_material == 0:
                materials.pop()
    if (made_boxes['Doll'] >=1 and made_boxes['Wooden train'] >= 1) or (made_boxes['Teddy bear'] >= 1 and made_boxes['Bicycle']>=1):
        succseed_boxes = True


if succseed_boxes:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if materials:
    result = reversed(materials)
    print(', '.join(str(el) for el in result))
if magics:
    print(reversed(magics))

[print(f"{k}: {v}") for k,v in sorted(made_boxes.items()) if made_boxes[k]>0]
