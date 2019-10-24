## Basic function definition and creation

def multi(a):
    b=a*a
    return b

##pass kiya static value into function and variable ko assign kiya
a=multi(5)
print(a)

##variable ko assign kiya value and pass kiya into function through print
k=15
c=print(multi(k))   

print(c) ## "None" --- C ki value none ho jaayegi after directly assigning it fucntion passing value through print
## its like print loop statements see below for reference
print(print(multi(k))) ## iska output bhi None aayega ( Andar waale ka 225 aayega because returned value once, baahar waale ka output none aayega because fucntion ek baar output return krta h)

##print se hi static value pass kiya function mein (through print ) 
print(multi(10))

# ## Addition function

def Add(a):
    print("Your input is %i"%a) ## takes passed input
    a+=a
    print("%i is your value after addition"%a) ## prints function after passing addition of input
    return a
    
k=10
print(Add(k))  ## it gives output as None as printing of function call gives None if there is no return in the function

print(print(Add(k))) ## it gives output as None as printing of function call returns only once in the function second return i.e. second loop of print fais and return None

## Exponentian function

def Exp(a,b):
    exp=a**b
    return exp

print(Exp(2,3))

