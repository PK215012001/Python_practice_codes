# generators are iterables which will not store elements in memory as list, instead it will
#  calculate results on demand
def square_numbers(nums):
    for i in nums:
        # whenevere yield comes it generates the result and stops execution
        yield i**2 

# nums_list = square_numbers([1,2,3,4,5])
# #  this will not print like list
# print(nums_list)
# # if we want elemenet from generator to be printed
# print(next(nums_list))
# print(next(nums_list))
# print(next(nums_list))
# print(next(nums_list))
# print(next(nums_list))
# #  we can able to iterate generator through list also
# for i in nums_list:
#     print(i)
#  we can create a generator using comprehensions as shown
nums_list = (x**2 for x in [1,2,3,4,5])
print(nums_list)
for i in nums_list:
    print(i)



