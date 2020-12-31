num1 = int(input())
num2 = int(input())
operator = input()
result = 0
output = 0

if num2 == 0:
    output = f'Cannot divide {num1} by zero'
elif operator == '/':
    result = (num1 / num2)
    output = f'{num1} {operator} {num2} = {result:.2f}'
elif operator == '%':
    result = num1 % num2
    output = f'{num1} {operator} {num2} = {result}'
else:
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    a = 'even' if result % 2 == 0 else 'odd'
    output = f'{num1} {operator} {num2} = {result} - {a}'

print(output)




