bitcoin = int (input())
juan = float(input())
commition = float(input())

EUR_to_bitcoin = bitcoin*1168/1.95
EUR_to_juan = juan*0.15*1.76/1.95
sum = EUR_to_bitcoin+EUR_to_juan
commition_in_procent = commition/100
commition_in_EUR = sum*commition_in_procent
result = (sum-commition_in_EUR)

print('%.2f' % result)