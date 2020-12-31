strings = input().split()
result = ''
for i in range(len(strings)):
    result += strings[i]*len(strings[i])

print(result)