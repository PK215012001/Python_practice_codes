# decorators are the functions which accepts other functions as arguments and add some
# functionality and returns other function without changing the source code of 
# the function we passed as an argument

# def decorated_function(original_func):
#     def wrapper_function():
#         print(f'wrapper executed this before:{original_func.__name__}')
#         return original_func()
#     return wrapper_function

# def display_func():
#     print('display function ran')
# display_func = decorated_function(display_func)
# display_func()
# #  if we observe above, even though we executed display_func(), it resulted in added
# # functionality of display_func() and we haven't even changed the original function
# # the same above can be written as below also by using keyword
# @decorated_function
# def sample_function():
#     print('sample function ran')

# sample_function()
# # by using keyowrd, we can directly execute our original function without calling our
# # decorated function seperatley
# # if our original functyion has arguments , then above will give error cause wrapper
# # function doesn't take any argumentys, for that we can pass arguments as shown below

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper function executed this before:{original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print(f'this function ran with arguments: {name} {age}')

display_info('pavan', 25)

# we can even decorate other functions also like this
@decorator_function
def display():
    print('display function ran')

display()

#  we can also use classes to decorate a function like below by using __call__ method
class LogDecorator:

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f'executing {self.original_function.__name__} with argument: {args} {kwargs}')
        return self.original_function(*args, **kwargs)
    
@LogDecorator
def multiply(x,y):
    print(x*y)
multiply(2,3)
