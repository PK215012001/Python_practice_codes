fav_movies = {'nolan' : 'memento', 'rajamouli': 'vikramarkudu', 'fincher' : 'gone girl', 'scorses': 'the irishman'}
print(fav_movies)
print(fav_movies.get('puri'))
print(fav_movies.get('puri', 'not found'))
fav_movies.update({'nolan' : 'dunkirk', 'puri' : 'pokiri'})
print(fav_movies)
del fav_movies['scorses']
print(fav_movies)
puri = fav_movies.pop('puri')
print(fav_movies)
print(puri)
print(len(fav_movies))
print(fav_movies.keys())
print(fav_movies.values())
print(fav_movies.items())
for movie in fav_movies:
    print(movie)

for movie in fav_movies.values():
    print(movie)