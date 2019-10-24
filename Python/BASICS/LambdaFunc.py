from functools import reduce


## Normal lambda function or Anonymous function
f= lambda a,b: a+b

result=f(2,4)
print(result)

## Filter with usual function
def is_even(n):
    return n%2==0

nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(is_even,nums))
print(evens)

##filter with lambda
evens=list(filter(lambda n: n%2==0 ,nums))
print(evens)

##map function without lambda
def do_doubles(n):
    return n*2

doubles=list(map(do_doubles,evens))
print(doubles)


##map function with lambda
doubles=list(map(lambda n:n*2,evens))
print(doubles)

##reduce function without lambda
def do_total(a,b):
    return a+b

sum1=reduce(do_total,doubles)

print(sum1)

## reduce function with lambda
sum1=reduce(lambda a,b:a+b,doubles)

print(sum1)