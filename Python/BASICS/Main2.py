##Importing main module and calling greeting function

import Main1 as MyAPI

MyAPI.greeting("Amit Yadav")

x=MyAPI.Player1["Jersey No."]
print(x)

## using paltform 
#3 discover system and many more
import platform as pf

a=pf.system()
print(a)

## finding dir
b=dir(pf)
print(b)


from Main1 import Player2 

c=Player2["Name"]
print(c)

import math 

print(math.pi)
print(math.pi/2)