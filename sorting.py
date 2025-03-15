nums_list = [23, 56, 15, 375, 46, 27, 10, 14]
#  sorted function will return us new variable
# print(sorted(nums_list))
# print(nums_list)
# # sort method sorts the list in place
# nums_list.sort()
# print(nums_list)
# print(sorted(nums_list, reverse= True))
# nums_list.sort(reverse= True)
# print(nums_list)
# sorted can be applied to any iterables
nums_tuple = (23, 56, 15, 375, 46, 27, 10, 14)
print(sorted(nums_tuple))
movie_dict = {'nolan': 'memento', 
              'fincher': 'gone girl', 
              'scorsese': 'the aviator', 
              'tarantino': 'pulp fiction', 
              'spielberg': 'schindlers list'}
print(sorted(movie_dict))
# by default sorted on dictionary will sort keys
# sorting based on absolute values
nums_list = [-4,-5,-6,1,2,3]
print(sorted(nums_list, key= abs))
# key takes function as arument and tells how we want to sort it

class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
    # __repr__ just used for representation of our objects of how we want
    def __repr__(self):
        return f'({self.name}, {self.age}, {self.pay})'

emp1 = Employee('pavan', 25, 40000)
emp2 = Employee('Vasanth', 26, 50000)
emp3 = Employee('Akshai', 24, 70000)
emp = [emp1, emp2, emp3]
print(emp)
print(sorted(emp, key= lambda x: x.name))
print(sorted(emp, key= lambda x: x.age))
# for classes we can directly use below
from operator import attrgetter
print(sorted(emp, key= attrgetter('age')))