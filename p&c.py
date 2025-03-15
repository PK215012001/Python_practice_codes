import itertools

my_list = [1,2,3]
# permutations
for i in itertools.permutations(my_list, 2):
    print(i)

# combinations
for i in itertools.combinations(my_list, 2):
    print(i)