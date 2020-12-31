student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    movie = input()
    if movie == 'Finish':
        break
    seats = int(input())
    all_tickets_sold = 0

    for i in range(1, seats + 1):
        type_ticket = input()

        if type_ticket == 'End':
            print(f'{movie} - {all_tickets_sold / seats * 100:.2f}% full.')
            break
        all_tickets_sold += 1

        if type_ticket == 'student':
            student_tickets += 1
        elif type_ticket == 'standard':
            standard_tickets += 1
        elif type_ticket == 'kid':
            kids_tickets += 1
        if all_tickets_sold == seats:
            print(f'{movie} - {all_tickets_sold / seats * 100:.2f}% full.')
            break

all_tickets = student_tickets + standard_tickets + kids_tickets
print(f"Total tickets: {student_tickets + standard_tickets + kids_tickets}")
print(f"{student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / all_tickets * 100:.2f}% kids tickets.")