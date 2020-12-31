books = input().split('&')

while True:
    line = input()
    if line == 'Done':
        break
    tokens = line.split(' | ')
    command = tokens[0]
    if command == 'Add Book':
        book_name = tokens[1]
        if book_name not in books:
            books.insert(0, book_name)

    elif command == 'Take Book':
        book_name = tokens[1]
        if book_name in books:
            books.remove(book_name)

    elif command == 'Swap Books':
        book1 = tokens[1]
        book2 = tokens[2]
        index1 = books.index(book1)
        index2 = books.index(book2)
        if book1 in books and book2 in books:
            books[index1], books[index2] = books[index2], books[index1]

    elif command == 'Insert Book':
        book_name = tokens[1]
        books.append(book_name)

    elif command == 'Check Book':
        index = int(tokens[1])
        if index in range(len(books)):
            print(books[index])

print(', '.join(books))