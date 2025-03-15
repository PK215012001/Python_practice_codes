# namedtuples are good middlegrounbd between dict and tuples and morereadable
from collections import namedtuple

Colors = namedtuple('colors', ['red', 'blue', 'green'])
color = Colors(255,160,245)
print(color[0])
print(color.blue)