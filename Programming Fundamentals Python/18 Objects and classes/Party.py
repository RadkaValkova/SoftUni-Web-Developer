# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
#
# while True:
#     line = input()
#     if line == 'End':
#         break
#     name = line
#     party.people.append(name)
#
# print(f"Going: {', '.join(party.people)}")
# print(f'Total: {len(party.people)}')

class Party:
    def __init__(self):
        self.people = []

    def invite(self, name):
        self.people.append(name)

    def names_of_all_people(self):
        return f'Going: {", ".join(self.people)}'

    def num_people(self):
        return f'Total: {len(self.people)}'


p = Party()

while True:
    line = input()
    if line == 'End':
        break
    name = line
    p.invite(name)

print(p.names_of_all_people())
print(p.num_people())
