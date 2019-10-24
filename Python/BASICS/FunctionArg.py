"""## no call by value and call by reference
 ## integer strings are immutable
def update(x):
    print(id(x))
    x=8
    print('x :',x)

a=10
print(id(a))
update(a)
print('a :',a) ## integer strings are immutable


def update(lst):
    print(id(lst))
    lst[3]=8
    print('x :',lst)

lst= [10,2,4,3]
print('a :',lst)
print(id(lst))
update(lst)
print('a :',lst)  ##list are mutable

## Types of Actual arguments :
#1.Position 
def person(name,age):  ## Formal arguments
    print(name)
    print(age)
                        ## Position can be changed here
person('AmitY',28)   ## Actual Arguemnts

#2.Keyword
def person(name,age):  
    print(name)
    print(age-5)

person('AmitY',age=28) ## keyword here is age 

#3.Default
def person(name,age=18):   ## age is passed as default as 18 if nothing is passed from actual arguments
    print(name)
    print(age)

person('AmitY') 

#4.Variable Length

def sum(a,*b): ## * in formal arguments
    print(a)
    print(b) ## creates tuple of variable length 
    c=a
    for e in b:
        c=c+e
    print(c)

sum(1,2,3,4) ## variable length actual argument

"""
def person(name,*data):   ## * in formal arguments
    print(name)
    print(data)         ## creates tuple of variable length 

person('Amit',25,'Mumbai',9021853340)  ## variable length actual argument

def person(name,**data):   ## ** depicts keyword length arguments in formal arguments
    print(name)
    print(data)           ## creates tuple of variable length 

person('Amit',age=25,city='Mumbai',Mob=9021853340)  ## with keywords variable length actual argument


def person(name,**data):   ## ** depicts keyword length arguments in formal arguments
    print(name)
    for (i,j) in data.items():
        print(i,j)          ## creates tuple of variable length 

person('Amit',age=25,city='Mumbai',Mob=9021853340)  ## with keywords variable length actual argument

