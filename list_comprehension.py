num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [n for n in num_list]
print(my_list)

even_list = [n for n in  num_list if n%2 == 0]
print(even_list)

alphanumeric_list = [{letter, num} for letter in 'abcd' for num in range(4)]
print(alphanumeric_list)

# dictionary comprehensions
directors = ['nolan', 'fincher', 'scorsese', 'tarantino', 'spielberg']
movies = ['memento', 'gone girl', 'the aviator', 'pulp fiction', 'schindlers list']
#  zip will form a list of tuples on one to one mapping
# movie_dict = {}
# for director, movie in zip(directors, movies):
#     movie_dict[director] = movie
# print(movie_dict)

# using dict comprehension
my_dict = {director: movie for director, movie in zip(directors, movies)}
print(my_dict)

#  set comprehensions
my_nums =  [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9]
my_set = {n for n in my_nums}
print(my_set)