# LEGB
# 'local, enclosing, global, buiiltin'

x = 'global x'

def test():
    # global x
    # x = 'local x'
    print(x)


test()
print(x)

#  enclosing example

# def outer():
#     x = 'outer x'
#     def inner():
#         #  alters the enclosing function variable from inside   
#         nonlocal x
#         x = 'inner x'
#         print(x)
#     inner()
#     print(x)

# outer()
      