pos= -1

def search(list,n):
    # print("Outside while: ",i)
    # print("Length of list: ",len(list))
    lb=0
    ub=len(list)-1

    while lb<=ub:
        mid=(lb+ub)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                lb=mid+1
            else:
                ub=mid-1
    return False
        

list=[4,7,8,12,45,99]
n=int(input("Enter the number to find in list: "))

if search(list,n):
    print("Found value at position %d" %(pos+1))
else:
    print("Not Found")


