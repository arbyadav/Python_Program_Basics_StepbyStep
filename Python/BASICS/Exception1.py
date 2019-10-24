## use try & except blocks

a=5
try:
    print(a,"is my output")
except NameError :
    print("a is not defined")
except:
    print("Error!!!")
finally:
    print("Exception is finished")