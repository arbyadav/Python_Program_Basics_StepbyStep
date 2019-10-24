class A:
    def __init__(self):
        print("I am constructor from class A")

    def featureA1(self):
        print('Feature A1 is working')

    def featureA2(self):
        print('Feature A2 is working')

class B(A):
    def __init__(self):
        super().__init__()
        print("I am constructor from class B")

    def featureB1(self):
        print('Feature B1 is working')
        
    def featureB2(self):
        print('Feature B2 is working')        


class C:
    def __init__(self):
        print("I am constructor from class C")

    def featureA1(self):
        print('Feature A1(C1) is working')
        
    def featureC2(self):
        print('Feature C2 is working')        


class D(A,C):
    def __init__(self):
        super().__init__()  ## this will class A init method not class C
        print("I am constructor from class D")

    def featureD1(self):
        print('Feature D1 is working')
        
    def featureD2(self):
        print('Feature D2 is working')
    
    def feat(self):
        super().featureA2()


d=D()
d.featureA1()
d.feat()
# a1.featureA1()
# a1.featureA2()

# b1=B()
# b1.featureA1()
# b1.featureA2()
# b1.featureB1()
# b1.featureB2() 
