class Car:
##namespace is an area where you create and store object/variable
    wheels=4  ## Class variable

    def __init__(self):
        print("I am Init")
        self.comp1='BMW'    ## Instance variables
        self.mil1=20        ## Instance variable

c1=Car()  ##CAR() is constructor

print(c1.comp1,c1.mil1,Car.wheels)
c1.comp1="AUDI"
c1.mil1=10

print(c1.comp1,c1.mil1,Car.wheels)