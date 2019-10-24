##using lambda function

x=lambda a: a+5
print(x(5)) ## works like a simple function with return value not visible

k=10
c=print(x(k)) ##call & passed value through print & variable k
print(c) ## as usual returns only once and give none type if stored and printed in a variable ( or use multiple print loops)

##lambda with multiple arguments

y= lambda a,b,c: a*b*c

print(y(1,2,3))
k=10
c=print(y(k,k,k)) ##call & passed value through print & variable k
print(c)  ## as usual returns only once and give none type if stored and printed in a variable ( or use multiple print loops)


def newmult(n) :
    return lambda b: b*n

newdouble=newmult(2) ## passes value to newmult function i.e value of n
print(newdouble(30)) ## passes value to lambda fucntion i.e value of b


def newadd(a,b) :
    return lambda x,y: x*a + y*b
    
newtwo=newadd(1,2) ##passes value to newadd fucntion i.e value of a & b
a=print(newtwo(5,4)) ##passes value to lambda fucntion i.e value of x & y

print(a) ## as usual returns only once and give none type if stored and printed in a variable ( or use multiple print loops)
