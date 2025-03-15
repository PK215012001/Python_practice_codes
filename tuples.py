# mutability

list_1 = [1, 2, 3, 4, 5]
list_2 = list_1
print(list_1)
print(list_2)
list_1[1] = 56
print(list_1)
print(list_2)


# immutability
tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
##tuple_1[0] = 45
print(tuple_1)
print(tuple_2)

set1 = {1, 2, 3, 4, 5}
print(set1)