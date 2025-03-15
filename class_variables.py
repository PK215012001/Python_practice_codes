# class variables are different from instance variables. Class variables can be accessed
#  by instances also
# But instance varibales are unique to each instance

class Employee:
    # class variables can be accessed by classes or instances also
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}{self.last}@company.com'
    #  function to apply raise without using class variables
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Pavan', 'kalyan', 80000)
emp2 = Employee('Vasanth', 'Kumar', 100000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.raise_amount)
#  we can access class variables through instances also, but if the instance contains
# same variable then it will first access from it, otherwise from class or inherited 
#  class
# print(emp1.raise_amount)
# print(emp2.raise_amount)
#  this gives the attributes of instance
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

#  if we change class variables by using class, it changes for instance also
Employee.apply_raise = 1.05
print(Employee.apply_raise)
print(emp1.apply_raise)
print(emp2.apply_raise)
#  but if we change it by using instance, then it will only change for that unique ins
emp1.apply_raise = 1.04
print(Employee.apply_raise)
print(emp1.apply_raise)
print(emp2.apply_raise)
emp1.favourite_movie = 'RRR'
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
