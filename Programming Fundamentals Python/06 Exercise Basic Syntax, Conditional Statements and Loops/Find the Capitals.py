word = input()
capital = []

for i in range(len(word)):
    letter = word[i]
    if letter.isupper():
        capital.append(i)
print(capital)

# word = input()
#
# capital_list = [i for i in range(len(word)) if word[i].isupper()]
#
# print(capital_list)