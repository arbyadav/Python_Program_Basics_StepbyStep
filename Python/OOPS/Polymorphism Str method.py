##Polymorph

class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
      
    def __str__(self):
        return self.m1+self.m2

s1=student(10,40)
s2=student(20,30)

print(s2.__str__())