#  a function which can be returned, passed as an argument or assigned it to a vraibel
#  is called a first class function
def square(x):
    return x**2
#  below is assigning a functions return value to a variable
f = square(5)
print(f)
#  below is assigning function itself to a vraible and we can use that variable same as
#  our original function
y = square
print(y)
print(y(2))

#  if a function accepts other fucntions as arguments and returns other arguments as 
# result, those are called higher order functions
# passing another function as an argument
def map_func(func, nums_list):
    new_list = []
    for i in nums_list:
        new_list.append(func(i))
    return new_list
nums_list = [1, 2, 3, 4, 5]
print(map_func(square,nums_list))
def cube(x):
    return x**3
print(map_func(cube, nums_list))

#  returning a function as a result
def operation(op):
    if (op == 'square'):
        return square
    elif(op == 'cube'):
        return cube
result = operation('cube')
print(result(5))

# another example
def logger(msg):
    def log_message():
        return(f'Hi!{msg}')
    return log_message

message = logger('world')
print(message())