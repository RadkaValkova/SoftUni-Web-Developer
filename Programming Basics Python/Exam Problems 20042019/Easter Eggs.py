eggs_number = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_color = - 100000
color = ''

for eggs in range(1, eggs_number + 1):
    current_color = input()
    if current_color == 'red':
        red += 1
        if red > max_color:
            max_color = red
            color = current_color
    elif current_color == 'orange':
        orange += 1
        if orange > max_color:
            max_color = orange
            color = current_color
    elif current_color == 'blue':
        blue += 1
        if blue > max_color:
            max_color = blue
            color = current_color
    elif current_color == 'green':
        green += 1
        if green > max_color:
            max_color = green
            color = current_color
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max_color} -> {color}')

