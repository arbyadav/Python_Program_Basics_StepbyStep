# class linearSearch:
pos= -1

def search(list,n):
    i=0
    print("Outside while: ",i)
    print("length of list: ",len(list))
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
        print("Inside while: ",i)

    return False
            
# c1=linearSearch()

list=[1,2,3,4,5,6]
n=int(input("Enter the number to find in list: "))

if search(list,n):
    print("Found value at position {}:",pos+1)
else:
    print("Not Found")


