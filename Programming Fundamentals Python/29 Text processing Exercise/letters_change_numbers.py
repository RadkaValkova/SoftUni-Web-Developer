def extract_result(let1,let2,num):
    result = 0
    if let1.isupper():
        result = num / (ord(let1)-64)
    else:
        result = num * (ord(let1)-96)
    if let2.isupper():
        result -= ord(let2)-64
    else:
        result += ord(let2)-96
    return result


line = input().split()

results = []

for i in range(len(line)):
    first_letter = line[i][0]
    last_letter = line[i][-1]
    number = int(line[i][1:-1])
    current_result = extract_result(first_letter,last_letter,number)
    results.append(current_result)

print(f'{sum(results):.2f}')
