days = int(input())
food = float(input())

bisqit = 0
sum_bisqit = 0
sum_dog_food = 0
sum_cat_food = 0

for i in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    day_food = dog_food + cat_food
    sum_dog_food += dog_food
    sum_cat_food += cat_food
    if i % 3 == 0:
        bisqit = (day_food) * 0.1
        sum_bisqit += bisqit

print(f'Total eaten biscuits: {round(sum_bisqit)}gr.')
print(f'{((sum_dog_food+sum_cat_food)/food*100):.2f}% of the food has been eaten.')
print(f'{(sum_dog_food/(sum_dog_food+sum_cat_food)*100):.2f}% eaten from the dog.')
print(f'{(sum_cat_food/(sum_dog_food+sum_cat_food)*100):.2f}% eaten from the cat.')
