###types of numbers

# print(type(2)) ##int
# print(type(-1)) ##int
# print(type(None)) ##Nonetype
# print(type(True)) ##bool
# print(type(-2.566)) ##float
# print(type(2-5j)) ##complex
# print(type('j')) ##str

import random

a=print(random.random()) #prints (float )random number between 0 & 1
b=print(random.randint(5,10)) #randint prints random number between given range
c=print(random.choice([1,2,3,4,5])) #choice prints random number between chosen number in sequence

print(type(a),type(b),type(c))

##oct & hex functions

x=10
print(hex(x),oct(x))