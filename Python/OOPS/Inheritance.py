## Using inheritance in python

class Person:
    def __init__(self,first,last):
        self.firstname=first
        self.lastname=last

    def fullName(self):
        return self.firstname+","+self.lastname

class Player(Person):
    def __init__(self,first,last,shirtnumber):
        Person.__init__(self,first,last)
        self.bushatnumber=shirtnumber
    
    def getplayer(self):
        print(self.fullName(),self.bushatnumber)
        return self.fullName()+","+self.bushatnumber


a=Person("Amit","Yadav")
# b=Player("Rohit","Sharma",11)  ## concat str + int error
c=Player("Yuvraj","Singh",'12')


print(a.fullName())
# print(b.getplayer())  ## concat str + int error
print(c.getplayer())

