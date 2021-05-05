clock_cycles = [int(el) for el in input().split(', ')]
job_index = int(input())


job_value = clock_cycles[job_index]
result = 0
for i in range(len(clock_cycles)):
    current_el = clock_cycles[i]
    current_ind = i
    if current_el < job_value:
        result += current_el
    if current_el == job_value:
        if current_ind <= job_index:
            result += clock_cycles[i]

print(result)

# numbers = [int(el) for el in input().split(', ')]
# index = int(input())
#
# numbers = enumerate(numbers)
# new_list = sorted(numbers, key= lambda x: x[1])   # sorted_numbers = sorted([(v,i) for (i,v) in enumerate(numbers)])
# total_time = 0
#
# for i in range(len(new_list)):
#     total_time += new_list[i][1]
#     if new_list[i][0] == index:
#         break
#
# print(total_time)