message = "Pk's world"
print(message)
message = 'Pk"s world'
print(message)
message = 'Pk\'s world'
print(message)
message = "Pk\"s world"
print(message)
favourite_movie = "Rajamouli's best movie is \"magadheera\""
print(favourite_movie)
favourite_movie = 'Rajamouli\'s best movie is "magadheera"'
print(favourite_movie)
print(len(favourite_movie))
print(message.upper())
print(message.capitalize())
print(message.casefold())
print(message.lower())
message = 'lllll'
print(message.count('l'))
message = 'Hello World'
print(message.replace('World', 'PK'))
print(message.lower())
print(message)

message = '     fdjkgdf     '
print(message)
print(message.strip())

name = 'pavan"s kalyan'
first, last = name.split('"s')
print(first)
print(last)
value = 3.1245864
print(round(value, 5))
print(f"{value:.5f}")

name = 'pavan'
print(name.rjust(10, '#'))
print(name.ljust(10, '#'))
print(name.center(11, '#'))