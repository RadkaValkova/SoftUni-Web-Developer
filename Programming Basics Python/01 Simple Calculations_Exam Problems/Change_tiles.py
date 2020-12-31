n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())
area_pl = n*n
area_bench = m*o
area_tile = w*l
area_to_cover = area_pl-area_bench
quontity = (area_to_cover/area_tile)
time = quontity*0.2

print(f'The quontity of tails is {quontity:.2f}.')
print(f'The time is {time:.2f}.')


