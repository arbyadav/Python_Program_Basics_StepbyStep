class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    
    def show(self):
        print(self.name , self.rollno)
        self.lap.show()
    
    class laptop:

        def __init__(self):
            self.brand="Apple"
            self.cpu='Mac OS'
            self.ram=8

        def show(self):
            print(self.brand , self.cpu, self.ram)

s1=Student('Marvin',2)
s2=Student('Jenny',10)
s1.show()
s2.show()