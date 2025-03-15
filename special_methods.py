# __repr__, __str__ are special methods which will implicitly called

class Employee():
    no_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    #  it is used to give data clearly for developers not for end users
    def __repr__(self):
        return f'Employee({self.first, self.last, self.pay})'
    #  it is used to give data clearly to end users, if both str and repr are defined
    #  then python will iplicitly call str
    # if str is missing then repr will be called automatically even if we use str
    def __str__(self):
        return f'{self.first} {self.last} pay is {self.pay}'
    
    #  we can even create arithmetic special methods for operator overloading
    #  below method will add salaries of two employee objects
    def __add__(self, other):
        return (self.pay + other.pay)


emp1 = Employee('pavan', 'kalyan', 40000)
emp2 = Employee('vasanth', 'kumar', 50000)
#  without repr or str method, below will print the objects location
print(emp1)
print(repr(emp1))
print(str(emp1))
print(emp1 + emp2)