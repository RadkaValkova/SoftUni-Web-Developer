sequence = input()

firs_half = sequence[:len(sequence)//2]
second_half = sequence[len(sequence)//2:]

st = []

for i in range(len(firs_half)):
    if firs_half[i] == '{':
        st.append('}')
    elif firs_half[i] == '[':
        st.append(']')
    elif firs_half[i] == '(':
        st.append(')')

result = ''
for i in range(len(st)):
    result += st.pop()

if result == second_half:
    print('YES')
else:
    print('NO')


