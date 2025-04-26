# statidc methods arre those methods which will not take either class or object as a parameter
# class methods are those methods awhich will take class as an argument

class Employee:
    '''An employee class'''
    no_of_emps = 0
    rasie_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self. email = f'{first}{last}@company.com'
    
    
    def apply_rasie(self):
        self.pay = self.pay * Employee.rasie_amount 
    
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.rasie_amount = amount
    
    # Another way to instantiate an object by using classmethod as constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # staticmethod use when the data it is taking doesn't either depend on object or class
    @staticmethod
    def is_workday(date):
        if (date.weekday() == 5 or date.weekday() == 6):
            return False
        return True


emp1 = Employee('pavan', 'kalyan', 90000)
emp2 = Employee('Vasanth', 'Kumar', 100000)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
print(emp1.rasie_amount)
print(emp2.rasie_amount)
print(Employee.rasie_amount)
print(emp1.pay)
print(emp2.pay)
emp1.apply_rasie()
emp2.apply_rasie()
print(emp1.pay)
print(emp2.pay)
Employee.set_raise_amnt(1.10)
print(emp1.rasie_amount)
print(emp2.rasie_amount)
print(Employee.rasie_amount)
emp1.apply_rasie()
emp2.apply_rasie()
print(emp1.pay)
print(emp2.pay)
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)
emp1_str = 'abhishek-redddy-90000'
emp2_str = 'kishor-reddy-80000'
emp3 = Employee.from_string(emp1_str)
emp4 = Employee.from_string(emp2_str)
print(emp3.__dict__)
print(emp4.__dict__)
import datetime
my_date = datetime.date(2025,3,22)
print(Employee.is_workday(my_date))