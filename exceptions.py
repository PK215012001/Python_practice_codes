try:
    # print(int('abcd'))
# we can raise our own exceptions as shown
#  nothing wrong below, but just raising my own exception
    x = 2
    if(x == 2):
        raise Exception
#  try to  use specific exceptions as posssible, because it helps them to easily catch it
except Exception:
    print('Not an integer')
else:
    print('k')
# else will execute if no exception is found
# finally will execute no matter what whether exception is found or not
finally:
    print(2)