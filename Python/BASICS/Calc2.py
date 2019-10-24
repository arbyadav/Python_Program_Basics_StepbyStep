##import module name through special variable
from Calc1 import *

def add1() :
    add()
    print("I am addition of"+' '+__name__)

def sub1() :
    print("I am subtraction of"+' '+__name__)

def main():
    add1()
    sub1()

main()