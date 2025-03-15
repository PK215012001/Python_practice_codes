# pythonic way and non pythonic way
# non pythonic way
# person = {'name': 'Pavan', 'age': 25, 'salary': 40000}
person = {'name': 'Pavan', 'age': 25}

# if ('name' in person and 'age' in person and 'salary' in person):
#     print(f'My name is {person["name"]}, age is {person["age"]} and salary is {person["salary"]}')
# else:
#     print('Missing some keys') 
# Pythonic way
try:
    print(f'My name is {person["name"]}, age is {person["age"]} and salary is {person["salary"]}')
except KeyError as e:
    print(f'Missing key: {e}')