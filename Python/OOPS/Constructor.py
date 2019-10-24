class person() :
    def __init__(self):
        self.name='Amit'
        self.age=25
    
    def update(self):
        self.age=25
    
    def compare(self,otherobj):
        if self.age==otherobj.age:
            return True
        else:
            return False


p1=person()
p2=person()

p1.name="Ankan"
p1.age=28

p1.update()

print(p1.name,p1.age)
print(p2.name,p2.age)

if p1.compare(p2) :
    print("Age is same")
else :
    print("Age is different")