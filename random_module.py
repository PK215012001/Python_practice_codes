# Gives random values between the things we want

import random
# gives value between 0, 1 and 1 not included
value = random.random()
print(value)
# uniform gives a float between a range
value = random.uniform(1, 10)
print(value)
value = random.randint(1,6)
print(value)
movies = ['rrr', 'eega', 'bahubali', 'memento']
value = random.choice(movies)
print(value)
colors = ['red', 'blue', 'green']
# choices function will gives us the list of no.of times we want some value
result = random.choices(colors, k= 25)
print(result)
# we can even give weightage to the numbers we want
result = random.choices(colors, weights= [18, 18, 2], k= 10)
print(result)
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)
# to choose a multiple numbers at a time randomly from a sample without being repeated
hand = random.sample(deck, k= 5)
print(hand)