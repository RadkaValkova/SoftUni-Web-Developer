import math                # дава ми 94т и рънтайм ерор на последната проверка
n = int(input())

prime = True

for i in range (2, int(math.sqrt(n))+1):
    if n % i == 0:
        prime = False
        break
if prime and n > 1:
    print('Prime')
else:
    print('Not prime')
