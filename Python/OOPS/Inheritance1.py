class A:
    def featureA1(self):
        print('Feature A1 is working')

    def featureA2(self):
        print('Feature A2 is working')

class B(A):                          ##Single level Inheritance B inherits A ( B has all features of A)
    def featureB1(self):
        print('Feature B1 is working')
        
    def featureB2(self):
        print('Feature B2 is working')        

class C(B):                         ## Multi level heritance C inherits B inherits A ( C has all features of A & B)
    def featureC1(self):
        print('Feature C1 is working')
        
    def featureC2(self):
        print('Feature C2 is working')  

a1=A()
a1.featureA1()
a1.featureA2()

b1=B()
b1.featureA1()
b1.featureA2()
b1.featureB1()
b1.featureB2() 


c1=C()
c1.featureA1()
c1.featureA2()
c1.featureB1()
c1.featureB2()
c1.featureC1()
c1.featureC2()

class D:
    def featureD1(self):
        print('Feature D1 is working')

    def featureD2(self):
        print('Feature D2 is working')

class E(A,D):                   ##Mutliple level inheritance (E inheritss both A & D)
    def featureE1(self):
        print('Feature E1 is working')

    def featureE2(self):
        print('Feature E2 is working')

e1=E()
e1.featureA1()
e1.featureA2()
e1.featureD1()
e1.featureD2()
e1.featureE1()
e1.featureE2()


