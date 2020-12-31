movie_name = input()
student_count = 0
standard_count = 0
kid_count = 0
total_tickets = 0

while movie_name != 'Finish':
    free_places = int(input())
    num_tickets = 0
    for i in range(1,free_places+1):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            student_count += 1
        elif ticket_type == 'standard':
            standard_count += 1
        elif ticket_type == 'kid':
            kid_count += 1
        num_tickets += 1
    print(f'{movie_name} - {num_tickets/free_places*100:.2f}% full.')
    movie_name = input()

total_tickets = student_count + standard_count + kid_count
print(f'Total tickets: {total_tickets}')
print(f'{student_count/total_tickets*100:.2f}% student tickets.')
print(f'{standard_count/total_tickets*100:.2f}% standard tickets.')
print(f'{kid_count / total_tickets * 100:.2f}% kids tickets.')
