def greet_user(greet, name, expression = '!'):
    return f'{greet} {name} {expression}'

print(greet_user('Hello', 'Pk'))

def movies(*movie_names):       # can be able to pass arbitrary no.of arguments and all will be collected inside a tuple
    print(movie_names)

movies('pokiri', 'rrr')

def fav_movies(**movie_names):      # can be able to pass any no of keyword arguments and will be stored as a dictionary
    print(movie_names)

fav_movies(nolan = 'memnto', rajamouli = 'rrr')

def greet_users(*names):
    for name in names:
        print(f'Hello {name}')

greet_users('pavan', 'kalyan')

def student_info(**info):
    for key, values in info.items():
        print(f'The info {key} of the current student is: {values}')

student_info(name = 'Pavan', age = 24, role = 'AI')