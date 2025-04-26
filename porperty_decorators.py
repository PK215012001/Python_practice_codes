class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.fullname = f'{first}{last}'
    
    # by using this we can access this method as an atribue
    @property
    def fullname(self):
        return f'{self.first}{self.last}'
    
    @property
    def get_email(self):
        return f'{self.first}.{self.last}@company.com'


emp1 = Employee('Pavan', 'Kalyan', 20000)
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.get_email())    
emp1.first = 'vasanth'    
print(emp1.first)
print(emp1.last)
print(emp1.fullname)
print(emp1.get_email())
emp1.fullname = 'Abhishek Reddy'
print(emp1.get_email)