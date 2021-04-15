def get_subexpression(expression):
    st = []
    result = []
    for index in range(len(expression)):
        ind = expression[index]
        if ind == '(':
            st.append(index)
        elif ind == ')':
            start_index = st.pop()
            subexpression = expression[start_index:index+1]
            result.append(subexpression)
    return result


expression = input()
for el in get_subexpression(expression):
    print(el)

line = input()

# opening_brackets = []
# for index in range(len(line)):
#     if line[index] == '(':
#         opening_brackets.append(index)
#     elif line[index] == ')':
#         start_index = opening_brackets.pop()
#         end_index = index
#         substring = line[start_index:end_index+1]
#         print(substring)