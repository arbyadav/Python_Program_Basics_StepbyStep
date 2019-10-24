class student:

    school="ST. Joseph"

    def __init__(self,m1,m2,m3):  ## init method ( constructor )
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):      ## instance methods
        return (self.m1 +self.m2+self.m3)/3
    
    def get_m1(self):   ##Accessors method (get method)
        return self.m1

    def set_m1 (self,value):  ## Mutators,method (set method)
        self.m1=value

    @classmethod
    def getSchool (cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is student class with me this as static method")

s1=student(10,20,30)

s2=student(20,40,50)

print(s1.avg())
print(s2.avg())
print(student.getSchool())
s1.info()