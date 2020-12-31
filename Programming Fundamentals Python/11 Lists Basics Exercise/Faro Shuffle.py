cards = input().split()
shuffle_number = int(input())

for i in range(shuffle_number):
    new_cards = []
    for y in range(len(cards)//2):
        first_card = cards[y]
        second_card = cards[y + len(cards)//2]
        new_cards.append(first_card)
        new_cards.append(second_card)
    cards_list = new_cards
print(cards)

# for i in range(shuffle_number):
#     first_half = []
#     second_half = []
#     new_cards = []
#     for j in range(0, len(cards) // 2):
#         first_half.append(cards[j])
#     for m in range(len(cards) // 2, len(cards)):
#         second_half.append(cards[m])
#
#     for k in range(len(first_half)):
#         new_cards.append(first_half[k])
#         new_cards.append(second_half[k])
#     cards = new_cards
# print(cards)
