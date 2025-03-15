#  we can inherit the attributes and methods from exisiting classes if we want to use them or override them
#  or add new functionality by using inheritance

class Employee:

    raise_amt = 1.2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
    
    def fullname(self):
        return f'{self.first}{self.last}'
    
    def set_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#  let's say we have 2 types of employees, developers and managers, we can create new classes using inheritance
#  like below

class Developers(Employee):
    raise_amt = 1.5
    
    def __init__(self, first, last, pay, prog_lang):
        #  super.() automatically makes use of employees init method to initialise objects first, last etc
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev1 = Developers('Corey', 'Schaffer', 40000, 'c')
print(dev1.email)
#  help, will show the method resolution order that is priority of the attributes and methods it is taking
# print(help(dev1))

dev1.set_raise()
print(dev1.pay)
dev2 = Developers('pavan', 'kalyan', 50000, 'python')
print(dev2.prog_lang)

#  creating an manager class which has employee data and the employees he manages

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    #  a method to add an employee to the given manager
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # a method to remove an existing employee from manager
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # a method to print the names of all employees under a manager
    def print_emps(self):
        for emp in self.employees:
            print(f'--> {emp.fullname()}')

mgr1 = Manager('shyial', 'essay', 100000, [dev1])
print(mgr1.email)
mgr1.print_emps()
mgr1.remove_emp(dev1)
mgr1.print_emps()
mgr1.add_emp(dev2)
mgr1.print_emps()

print(isinstance(mgr1, Employee))
print(issubclass(Developers, Employee))