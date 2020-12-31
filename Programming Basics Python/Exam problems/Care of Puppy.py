available_food_kg = int(input())
available_food_gr = available_food_kg * 1000
eaten_food = 0

while True:
    line = input()
    if line == 'Adopted':
        if available_food_gr >= eaten_food:
            print(f'Food is enough! Leftovers: {available_food_gr - eaten_food} grams.')
        else:
            print(f'Food is not enough. You need {eaten_food - available_food_gr} grams more.')
        break
    food = int(line)
    eaten_food += food
