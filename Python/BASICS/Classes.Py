##using class key word and creating classes

class FirstClass:
    a=15

print("My class type is",FirstClass) ## prints class type
obj1=FirstClass()
print(obj1.a)

## using init function

class Players:
    def __init__(self,number,age):
        self.number=number
        self.age=age
    def newFunc(self,area):
        return area*area

    def newalt(self,a,b):
        return a+b

obj2=Players(5,23)
print("Player Number is",obj2.number,"and","Age is",obj2.age)
print("Total area is",obj2.newFunc(50),"Square metre" )
print("Total sum",obj2.newalt(8,3))