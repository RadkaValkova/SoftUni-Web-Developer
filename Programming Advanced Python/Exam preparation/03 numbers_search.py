def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)
    missing_num = 0
    duplicate_nums = []
    for i in range(min_num,max_num+1):
        if i not in args:
            missing_num = i
        if args.count(i) > 1:
            duplicate_nums.append(i)
    return [missing_num, sorted(duplicate_nums)]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))