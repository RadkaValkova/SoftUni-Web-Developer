n = int(input())
intersection_list = []

max_len = - 1000000
max_intersection = ''

for _ in range(n):
    (first,second) = input().split('-')
    start1 = int(first.split(',')[0])
    end1 = int(first.split(',')[1])
    start2 = int(second.split(',')[0])
    end2 = int(second.split(',')[1])
    first_set = set([el for el in range(start1, end1+1)])
    second_set = set([el for el in range(start2, end2+1)])
    intersection = first_set.intersection(second_set)
    intersection_list.append(intersection)

for i in range(len(intersection_list)):
    if len(intersection_list[i]) > max_len:
        max_len = len(intersection_list[i])
        max_intersection = intersection_list[i]

print(f'Longest intersection is {[x for x in max_intersection]} with length {max_len}')