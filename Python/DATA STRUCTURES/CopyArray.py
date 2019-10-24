from numpy import *

arr1=array([1,4,3,6,5])

arr1+=5

print(arr1)


arr2=array([4,5,6,7,8])

arr3=arr1+arr2
print(arr3)
print(sum(arr1))
print(min(arr1))
print(max(arr1))
print(sin(arr1))
print(cos(arr1))
print(log(arr1))
print(sort(arr1))

print(concatenate([arr1,arr2]))

arr6=arr1
print(arr6)

print(id(arr1),id(arr6))

arr7=arr1.view() ## view does shadow copy i.e if changed value of one array it will be changed to second too
arr1[1]=8
print(arr1, arr7)
print(id(arr1),id(arr7))

arr8=arr1.copy() ##Copies array but no shadow copy i.e if changed value of array after copyin will remain same for other array
arr1[1]=4
print(arr1,arr8)
print(id(arr1),id(arr8))

