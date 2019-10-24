a=5
print(" A is 5,now go & divide")
try:
    print("Resource Open")
    k=int(input("Enter a number "))
    print(k)    
    print('Output is',a/k)  ## critical statement if zero comes in
    # print("Resource Closed") ....don't close it here
except ZeroDivisionError as e:
    print("Hey, you cannot divide the number by zero ", e)
except ValueError as v:
    print("Invalid Input ",v)
except Exception as ex:
    print("Something went wrong...")

    # print("Resource Closed") ....don't close it here

finally:
    print("Resource Closed") 

