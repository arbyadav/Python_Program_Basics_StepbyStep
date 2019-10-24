# import array as arr
from array import *

# uarr=arr.array('i',[1,2,3])

# print(uarr)

arr=array('i',[])

n=int(input("Enter the lenth of array\n"))

for i in range(n):
    x=int(input("Enter the next value\n"))
    arr.append(x)

print(arr)

searchval=int(input("Enter the value to search\n"))

k=0
for i in arr:
    if i==searchval:
        print("Value is at index",k)
        break
    k+=1

print(arr.index(searchval))