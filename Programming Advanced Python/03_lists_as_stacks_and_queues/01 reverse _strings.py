def reverse_text(text):
    st = []
    for ch in text:
        st.append(ch)

    reversed_text = []
    while st:
        reversed_text.append(st.pop())
    result = ''.join(reversed_text)
    return result


text = input()
print(reverse_text(text))