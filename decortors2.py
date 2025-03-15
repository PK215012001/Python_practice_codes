# decorators are mainly used for logging and timing uses

def logging_function(original_function):
    import logging
    logging.basicConfig(filename= f'{original_function.__name__}.log', level= logging.INFO)
    def  wrapper_function(*args, **kwargs):
        logging.info(f'Ran with args {args} and kwargs {kwargs}')
        return original_function(*args, **kwargs)
    return wrapper_function

@logging_function
def add(x,y,z):
    print(x+y+z)

add(4,5,6)
add(7,8,9)

# timing example

class timing_decorator:

    def __init__(self, originial_function):
        self.originial_function = originial_function
    
    def __call__(self, *args, **kwds):
        import time
        t1 = time.time()
        result = self.originial_function(*args, **kwds)
        t2 = time.time() - t1
        print(f'{self.originial_function.__name__} ran in: {t2} secs')
        return result

@timing_decorator
def square(x):
    return(x**2)
print(square(2))

