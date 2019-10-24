#dictionaries in python represented by {} Curly bracket
###dictionaries are mutable
##value can be given in key value pairs in dictionaries

##dictionaries in dictionaries
dict1={"PLAYER1":10,"PLAYER2":30,"PLAYER3":50}
print(type(dict1))
print(dict1)

dict2={1,2,3} ## this is set in curly braces not a dictionary check its types to confirm
print(type(dict2)) ## random display krta h dictionaries if there is no other dictionaries
print(dict2)

# ##lists & tuples in dictionaries
dict3={"Animals":['horse','rabbit'],"Birds":('parrot','sparrow')}
print(dict3["Animals"])
print(dict3.get("animals")) ## Case sensitive hai small 'a' nhi chalta capital 'A" ki jagah pe , agar get method se kiye toh , None return dega instead of exception key error
print(dict3.get("Animals"))
print(dict3.get("Animals","Birds")) #3 it will print only 1st key accessed

## it is mutable as we can change dictionaries value
dict3["Animals"][1]='KHARGOSH'
print(dict3["Animals"][1])
print(dict3.get("Animals"))

## NEW ITEM IN DICTIONARY
dict3["Numbers"]=1,2
print(dict3)
## del dict1

## print(animals_tuple1)


