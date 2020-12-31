size = float(input())
sours_Metric = input()
dest_Metric = input()

if sours_Metric == 'mm':
    size = size / 1000
elif sours_Metric == 'cm':
    size = size / 100
elif sours_Metric == 'mi':
    size = size / 0.000621371192
elif sours_Metric == 'in':
    size = size / 39.3700787
elif sours_Metric == 'km':
    size = size / 0.001
elif sours_Metric == 'ft':
    size = size / 3.2808399
elif sours_Metric == 'yd':
    size = size / 1.0936133

if dest_Metric == 'mm':
    size = size * 1000
elif dest_Metric == 'cm':
    size = size * 100
elif dest_Metric == 'cm':
    size = size * 100
elif dest_Metric == 'mi':
    size = size * 0.000621371192
elif dest_Metric == 'in':
    size = size * 39.3700787
elif dest_Metric == 'km':
    size = size * 0.001
elif dest_Metric == 'ft':
    size = size * 3.2808399
elif dest_Metric == 'yd':
    size = size * 1.0936133

print(f'{size} {dest_Metric}')