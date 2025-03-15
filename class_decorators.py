#  we can even use classes to decorate our functions
#  instead of passing a function as an argument to our decorator function, here we will
#  use __intit__ method to define our decorator function and use __call__ method
#  for wrapper function

class Decorator(object):

    def __init__(self, original_func):
        self.original_func = original_func
    def __call__(self, *args, **kwargs):
        print(f'The function before decoration prints this: ')
        return self.original_func(*args, **kwargs)
@Decorator
def display():
    print(f'Hi')

@Decorator
def display_info(name, age):
    print(f'This function takes arguments as {name} {age}')

display()
display_info('pavan', 24)