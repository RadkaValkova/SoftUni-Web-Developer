import sys
movie_number = int(input())
max_rate = -sys.maxsize
min_rate = sys.maxsize
sum_rates = 0
max_name = ''
min_name = ''

for i in range(1, movie_number+1):
    movie_name = input()
    movie_rate = float(input())
    if movie_rate > max_rate:
        max_rate = movie_rate
        max_name = movie_name
    if movie_rate < min_rate:
        min_rate = movie_rate
        min_name = movie_name
    sum_rates += movie_rate
average = sum_rates/movie_number
print(f'{max_name} is with highest rating: {max_rate:.1f}')
print(f'{min_name} is with lowest rating: {min_rate:.1f}')
print(f'Average rating: {average:.1f}')
