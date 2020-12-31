import math
cakes_number = int(input())
total_sugar = 0
total_flour = 0
max_sugar = -100000000
max_flour = -100000000

for i in range(1, cakes_number + 1):
    sugar = int(input())
    flour = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
    total_sugar += sugar
    total_flour += flour
package_sugar = math.ceil(total_sugar / 950)
package_flour = math.ceil(total_flour / 750)

print(f'Sugar: {package_sugar}')
print(f'Flour: {package_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')

