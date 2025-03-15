# 

def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func
hi_func = outer_func('hi')
hello_func = outer_func('Hello')
hi_func()
hello_func()

import logging
logging.basicConfig(filename= 'closures.py', level= logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f'Running {func.__name__} with arguments {args}')
        print(func(*args))
    return log_func

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def square(x):
    return x**2
def cube(x):
    return x**3

add_logger = logger(add)
add_logger(2,3)
logger(sub)(3,4)
logger(square)(5)
logger(cube)(4)