integers = input().split(' ')

st = [el for el in integers]

result = []
while st:
    result.append(st.pop())
print(' '.join(result))
