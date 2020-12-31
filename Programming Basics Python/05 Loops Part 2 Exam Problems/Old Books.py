fav_book = input()
book = input()
book_count = 0
is_found = True

while book != fav_book:
    book_count += 1
    if book == 'No More Books':
        is_found = False
        break
    book = input()
if is_found:
    print(f'You checked {book_count} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f'You checked {book_count} books.')

# favorite_book = input()
#
# book_count = 0
# while True:
#     book = input()
#     if book == 'No More Books':
#         print('The book you search is not here!')
#         print(f'You checked {book_count} books.')
#         break
#     if book == favorite_book:
#         print(f'You checked {book_count} books and found it.')
#         break
#     book_count += 1