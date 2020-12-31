pen = int(input())
marker = int(input())
cleaner = float(input())
discount = int(input())

sum_pen = pen*5.8
sum_marker = marker*7.2
sum_cleaner = cleaner*1.2
totsl_sum = sum_pen+sum_marker+sum_cleaner
discount_lv = totsl_sum*(discount/100)
final_sum = totsl_sum-discount_lv

print('%.3f' % final_sum)
