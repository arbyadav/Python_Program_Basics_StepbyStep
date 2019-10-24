##absolute value function
print(abs(2.5))
print(abs(-2.56))
print(abs(2+7j))

##all value function returns true if all 1
print(all([1,1,0]))
print(all([1,1,1]))

##binary conversion function
print(bin(5))

##order function
print(ord("h"))

##check if it is a callable function
def fun(a, b):
    s=a*b
    return s
print(callable(fun))

##sum of all values function
print(sum([1,2,3]))

##convert to string function
print(str(5.7))

## Range function
x=range(2,10,2)
for n in x:
    print(n)

##slice function ( USING VARIABLE)

tuple=(1,"amity",3,5,6,8,9)
x=slice(4)
print(tuple[x])

##round the value function
print(round(3.1456))
print(round(3.1456,2))