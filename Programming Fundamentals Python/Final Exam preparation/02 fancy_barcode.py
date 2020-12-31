import re

n = int(input())
pattern = r'@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+'

matches_list = []

# for i in range(n):
#     barcode = input()
#     matches = re.findall(pattern,barcode)
#     if matches:
#         bar = [matches[0][i] for i in range(len(matches[0])) if matches[0][i].isdigit()]
#         if len(bar) != 0:
#             print(f'Product group: {"".join(bar)}')
#         else:
#             print('Product group: 00')
#     else:
#         print('Invalid barcode')

for _ in range(n):
    barcode = input()
    if re.match(pattern, barcode):
        digits = re.findall(r'\d', barcode)
        if digits:
            print(f'Product group: {"".join(digits)}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')

