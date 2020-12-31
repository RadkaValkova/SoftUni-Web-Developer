voucher = int(input())
purchase_name = input()

ticket_cunt = 0
purchase_count = 0
purchase_price = 0

while purchase_name != 'End':
    if purchase_name == 'End':
        break
    if len(purchase_name) > 8:
        purchase_price = ord(purchase_name[0]) + ord(purchase_name[1])
        if voucher >= purchase_price:
            voucher -= purchase_price
        else:
            break
        ticket_cunt += 1
    else:
        purchase_price = ord(purchase_name[0])
        if voucher >= purchase_price:
            voucher -= purchase_price
        else:
            break
        purchase_count += 1
    purchase_name = input()

print(f'{ticket_cunt}')
print(f'{purchase_count}')



