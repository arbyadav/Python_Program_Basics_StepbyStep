#Create a new file
f=open("newfile.txt","x")

##append in a file
f=open("newfile.txt","a")
f.write("Hi I am python developer")
f.write("Hi new file")

##using read method
f=open("Newfile.txt",'r')
print(f.read())  ##read 
print(f.read(3)) #read number of characters
print(f.readline()) ## read line by line
print(f.readline()) ## read line by line
print(f.readline(3)) ## read as per characters of 3rd line if readline commands appears at number 3

## to remove or delete the file
import os
os.remove("newfile.txt")
