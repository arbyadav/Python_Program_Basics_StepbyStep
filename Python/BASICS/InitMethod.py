## PART 1  using init method as constructor
"""
class Computer:

    def __init__(self) :
        print("I am Init")
    
    def config(self):
        print("i5 gen, 16 gb RAM ")


com1=Computer()
com1.config()


##PART 2  using object to pass paramater to init mehtod 
 
class Computer:

    def __init__(self,cpu,ram) :
        print("I am Init")
        self.cpu1=cpu
        self.ram1=ram
    
    def config(self):
        print("i5 gen, 16 gb RAM ")
        print("%s %02d"%(self.cpu1,self.ram1)) 


com1=Computer("i7",32)

com1.config()
"""

##PART 3  using object & method in object to pass paramater to init mehtod  & object method
 
class Computer:

    def __init__(self,cpu,ram) :
        print("I am Init")
        self.cpu1=cpu
        self.ram1=ram
        print("%s %02d"%(self.cpu1,self.ram1)) 
    
    def config(self,cpu,ram):
        print("i5 gen, 16 gb RAM ")
        self.cpu2=cpu
        self.ram2=ram
        print("%s %02d"%(self.cpu2,self.ram2)) 

com1=Computer("i7",32)

com1.config("i9",64)
