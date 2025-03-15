class Duck:
    def quack(self):
        print(f'Quack, quack')

class Person:
    def quack(self):
        print(f'I am quacking like a duck')

def make_it_quack(object):
    # not duck typed(becuase for this function we are caring on the object type)
    if (isinstance(object, Duck)):
        object.quack()
    else:
        print('This has to be a duck')
duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)

#  Here if we observe make_it_quack will not care about the if it is person or duck
# as long as it coontains method quack
# in duck typing, object behaviour is determines its type rather than its class
# Here we don't check an object's type explicitly, instead we check wheteher
# it has the required attributes or methods, allows for more flexible and polymorphic
# def makequack(thing):
#     # duck typed because we don't care about the object, we just care about it's behaviour
#     thing.quack()
# duck2 = Duck()
# person2 = Person()
# makequack(duck2)
# makequack(person2)
# # But the above is sometimes dangerous which can cause errors because even though
# # it doesn't depend on object, but shouldn't we atleast check whether that function
# # is available to that object or not for better duck typing
# # here comes 2 methods, one if non-pythonic way(first check conditions and then do the task)
# def quack1(thing):
#     #  we are first checking whether the thing has attribute quack and whether it is callable
#     if (hasattr(thing, 'quack')):
#         if (callable(thing.quack)):
#             thing.quack()
# person3 = Person()
# quack1(person3)
# pythonic way, first try it if wrong, caught an error
def quack2(object):
    try:
        object.quack()
        object.bark()
    except AttributeError as e:
        print(e)

person4 = Person()
quack2(person4)