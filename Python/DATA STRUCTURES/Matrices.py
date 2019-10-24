from numpy import *

arr1=array([[1,2,3],[4,56,6]])

print(arr1)

print(arr1.shape) ## (row,columns)
print(arr1.size)  ## no of elements
print(arr1.ndim)  ## dim of array i.e here (2D)

arr2=arr1.flatten() ##Converts 3D or 2D arrays to 1D array

print(arr2)

arr3=arr2.reshape(3,2) ##reshapes 1D array to 2D or 3D arrays

print(arr3)


m1=matrix(arr1)
print(m1)
m2=arr1
print(m1)
m3=matrix('1 2 3; 5 4 6; 1 6 7')
print(m3)

print(m3.max())

print(m3.diagonal())
