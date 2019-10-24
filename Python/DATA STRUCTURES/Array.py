from array import *

## calling array function from array class
values=array('i',[1,2,8,3])
print(values)
print(values.typecode) ## type of code
print(values.buffer_info()) ## prints (addr,size)


values.reverse()

print(values[0])
print('\n')
##with values
for e in values:
    print(e)

##with range
for i in range(len(values)):
    print(values[i])

print('\n')
newArr=array(values.typecode,(a*a for a in values))

for e in newArr:
        print(e)

print('\n')

i=0
while(i<len(newArr)):
    print(newArr[i])
    i+=1