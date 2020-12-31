
movie_name = input()
days = int(input())
ticket_number = int(input())
price = float(input())
percent_cinema = int(input())

total_incomes = (days * ticket_number * price) - (days * ticket_number * price)*percent_cinema/100

print(f'The profit from the movie {movie_name} is {total_incomes:.2f} lv.')
