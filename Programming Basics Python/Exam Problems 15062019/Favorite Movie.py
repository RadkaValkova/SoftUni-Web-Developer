import sys
max_movie_points = -sys.maxsize
max_movie = ''
is_reached = True

for mov in range(1,7+1):
    movie = input()
    movie_points = 0
    if movie == 'STOP':
        is_reached = False
        break
    for let in movie:
        movie_points += ord(let)
    count_upper = 0
    count_lower = 0
    for letter in movie:
        if (letter.islower()) == True:
            count_lower += 1
        elif (letter.isupper()) == True:
            count_upper += 1
    movie_points = movie_points - (count_lower * 2 * len(movie)) - (count_upper * len(movie))
    if movie_points > max_movie_points:
        max_movie_points = movie_points
        max_movie = movie

if is_reached:
    print('The limit is reached.')
print(f'The best movie for you is {max_movie} with {max_movie_points} ASCII sum.')


