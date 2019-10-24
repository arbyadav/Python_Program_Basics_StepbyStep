from numpy import *

arr=array([1,2,3,4.0])
arr1=array([1,2,3,4],int)
print(arr)
print(arr.dtype)
print(arr1)
print(arr1.dtype)

## Linspace (start,stop, parts)

arr2=linspace(0,15,26)
arr2=linspace(0,15) ##default parts is 50
print(arr2)

##Arange (start,stop,skips)
arr3=arange(1,100,2)
print(arr3)

##Logspace()
arr4=logspace(1,40,5)
print(arr4)
print('%2f'%arr4[4])

#ones()
arr5=ones(5,int)
print(arr5)

#zeros()
arr6=zeros(5,int)

print(arr6)