# Programme to create some random passwords
import random

char_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*',
             '(', ')', '-', '_', '+', '=', '.']

for i in range(10000000):
    password = random.choices(char_list, k= 12)
    password = ''.join(password)
    print(password)