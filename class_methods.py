class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first}{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    #  weekday( function returns 0 for monday and 6 for sunday)
    def is_weekday(day):
        if(day.weekday() == 5 or day.weekday() == 6):
            return False
        else:
            return True
emp1 = Employee('Corey', 'Schaffer', 40000)
emp2 = Employee('pavan', 'kalyan', 50000)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

#  now we can change these values by using class methods also as shown
Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

#  we can even use instances to access it, but generally no use and not used that much
emp1.set_raise_amt(1.06)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

#  suppose our employee details are coming as create between hypens as shown, we can create objects like this
emp_str1 = 'pavan-kalyan-40000'
first, last, pay = emp_str1.split('-')
new_emp = Employee(first, last, pay)
print(new_emp.pay)
print(new_emp.raise_amt)

#  but we can also create it by using classmethods as it will automatically acts as constructor as shown above
emp2_str = 'vasanth-kumar-70000'
new_emp2 = Employee.from_str(emp2_str)
print(new_emp2.first)
print(new_emp2.pay)
print(new_emp2.raise_amt)


#  static methods are methods which don't take class or instances as arguments, those are created as above
import datetime
my_date = datetime.date(2025, 2, 17)
print(Employee.is_weekday(my_date))
print(emp1.is_weekday(my_date))