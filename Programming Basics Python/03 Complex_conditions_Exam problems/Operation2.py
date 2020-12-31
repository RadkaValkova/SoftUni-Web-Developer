n1 = int(input())
n2 = int(input())
operator = input()

result = 0
output = ''
if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/' and n2 != 0:
    result = n1 / n2
elif operator == '%' and n2 != 0:
    result = n1 % n2

if operator == '%' and n2 !=0:
    output = (f'{n1} {operator} {n2} = {result}')
elif (operator == '+' or operator == '-' or operator == '*'):
    if result % 2 == 0:
        output = (f'{n1} {operator} {n2} = {result} - even')
    else:
        output = ((f'{n1} {operator} {n2} = {result} - odd'))
elif operator == '/' and n2 != 0:
    output = (f'{n1} {operator} {n2} = {result:.2f}')
else:
    output = (f'Cannot divide {n1} by zero')

print(output)

