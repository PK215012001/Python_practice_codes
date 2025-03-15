# classes helps us to reuse the code and extend it

class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return f'{self.first}{self.last}'

#  below are instances of classes
# emp1 = Employee()
# emp2 = Employee()
# print(emp1)
# print(emp2)
# emp1.first = 'Pk'
# emp1.last = 'reddy'
# emp1.email = f'{emp1.first}{emp1.last}@company.com'
# emp2.first = 'Vasanth'
# emp2.last = 'kumar'
# emp2.email = f'{emp2.first}{emp2.last}@company.com'
# print(emp1.email)
# print(emp2.email)
#  we can directly set our variables while defining the class itslef as shown

class Movie:

    def __init__(self, name, director, hero):
        self.name = name
        self.director = director
        self.hero = hero

movie1 = Movie('Vikramarkudu', 'Rajamouli', "Ravi Teja")
movie2 = Movie('Pokiri', 'Puri Jagannath', 'Mahesh babu')
print(movie1.hero)
print(movie2.hero)
emp1 = Employee('Pavan', 'Kalyan', 40000)
print(emp1.fullname())
# another way to call functions
print(Employee.fullname(emp1))