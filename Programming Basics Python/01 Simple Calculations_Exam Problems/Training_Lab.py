lenght = float(input()) * 100
weidth = float(input()) * 100
rows = (lenght//120)
col = ((weidth-100)//70)
seats = rows * col-3
print('The seats are : ' + str(seats))

w = float(input())
h = float(input())
w_to_cm = h*100
h_to_cm = w*100

rows = int(w_to_cm/120)
col = int((h_to_cm-100)/70)
seats = rows * col-3
print('The seats are : ' + str(seats))