##For with in looping

##Looping through list
animals=['rabbit','mouse','cat','dog']

for x in animals:
    print(x)
print(callable(animals)) ## animals is non callable function

##Looping through for
for x in animals:
    print(x)

##for with break
for x in animals:
    print(x)
    if x=='mouse':
        break

##for with if else

for x in animals:
    print(x)
    if x=='mouse':
        print("sexy mouse")
    else:
        print("fuck you mouse")

##for with else

for x in animals:
    print(x)
else:
    print("Completed check")

## Looping through Dictionaries
Players={"Player1":"Amit","Player2":"Rohit","Player3":"Yuvi"}

for x in Players:
    print(x,Players[x])
print(callable(Players)) ## Players is non callable function
##Looping through Tuples
Aviators=("panchi","chidiya","bird")

for x in Aviators:
    print(x)
print(callable(Aviators)) ## Aviators is non callable function
    