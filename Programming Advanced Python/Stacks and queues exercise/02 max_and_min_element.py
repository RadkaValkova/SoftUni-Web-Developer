queries_number = int(input())

st = []

for _ in range(queries_number):
    line = input().split(' ')
    query = int(line[0])
    if query == 1:
        st.append(int(line[1]))
    elif query == 2:
        if len(st) > 0:
            st.pop()
    elif query == 3:
        if st:
            print(max(st))
    elif query == 4:
        if st:
            print(min(st))

print(', '.join([str(el) for el in reversed(st)]))

