days = int(input())
budget = float(input())
people = int(input())
price_fuel_per_km = float(input())
food_per_person = float(input())
room_for_night = float(input())
hotel = people * room_for_night * days
food = people * food_per_person * days

if people > 10:
    hotel = hotel * 0.75
expenses = hotel + food

for i in range(1,days+1):
    kilometers = float(input())
    expenses += kilometers * price_fuel_per_km

    if i % 3 == 0 or i % 5 == 0:
        expenses += expenses * 0.4
    if i % 7 == 0:
        expenses -= expenses / people
    if expenses > budget:
        print(f'Not enough money to continue the trip. You need {abs(budget-expenses):.2f}$ more.')
        break
if budget >= expenses:

    print(f'You have reached the destination. You have {(budget-expenses):.2f}$ budget left.')
