movies = ['magadheera', 'vikramarkudu', 'rrr', 'eega']
print(movies)
print(movies[0])
movies.append('bahubali')
print(movies)
movies.insert(3, 'yamadonga')
print(movies)
fav_movies = ['inception', 'memento', 'forrest gump']
movies.append(fav_movies)
print(movies)
movies.extend(fav_movies)
print(movies)
movies.remove('bahubali')
print(movies)
popped_movie = movies.pop(5)
print(movies)
print(popped_movie)
del movies[3]
print(movies)
num_list = [47, 28, 923, 570]
num_list.sort()
print(num_list)
num_list = [47, 28, 923, 570]
num_list.sort(reverse= True)
print(num_list)
num_list = [47, 28, 923, 570]
print(sorted(num_list))
print(sorted(num_list, reverse= True))
print(num_list)
print(min(num_list))
print(max(num_list))
print('bahubali' in movies)

for movie in movies:
    print(movie)

for index, movie in enumerate(movies, start= 2):
    print(index, movie)

movies_str = ' - '.join(movies)
print(movies_str)
new_movie_list = movies_str.split(' - ')
print(new_movie_list)
