days = int(input())
bakers = int(input())
cakes = int(input())
goffretes = int(input())
creps = int(input())

incomes_cakes = bakers * cakes * 45
incomes_goffretes = bakers * goffretes * 5.8
incomes_creps = bakers * creps * 3.2

total_incomes = (incomes_cakes + incomes_goffretes + incomes_creps)*days
materials = total_incomes * 1/8
rest = total_incomes - materials
print(rest)
