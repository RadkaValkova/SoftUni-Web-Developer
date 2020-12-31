garden_area=int(input())
price=7.61
total_price=(garden_area*price)
discount=total_price*0.18
print(f'The final price is : {(total_price-discount):.2f} lv.')
print(f'The discount is : {(discount):.2f} lv.')