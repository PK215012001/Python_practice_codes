class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        self.name = ''

p = Person('Pavan')
print(p.name)
del p.name
print(p.name)
p.name = 'Vasanth'
print(p.name)