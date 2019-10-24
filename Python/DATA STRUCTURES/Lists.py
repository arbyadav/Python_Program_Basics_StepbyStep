#Lists in python represented by [] square  bracket
###Lists are mutable


#LISTS
animals=['TIGER','LION','WOLF','DOG']
print(animals)

#list in lists
rl=['DOG',1,3,5,['amit','key','5','PYTHON']]
print(rl)

#length of list
print(len(rl))

# #callinglist by index
# a=animals[0]
# b=rl[4][3]
# print(b)

# #Range of items
# c=rl[0:3]
# print(c)

#last item
d=rl[-1]
print(d)

#change list item
rl[-2]='cat'
print(rl)

#append list item animals
animals.append('ELEPHANT')
print(animals) 

#delete items from list
del animals[3]
print(animals)