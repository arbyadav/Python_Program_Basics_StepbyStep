## conditional operator

### IF statement conditions ###

x=10
print('Bada hai x' if x>8  else 'chota hai x' )

y=10
if y>8:
    print("Y bada hai")
y=5
if y>10:
    print("Mein bada hoon yaar")
elif y>7:
    print("thoda sa aur chahiye yaar")  
else:
    print("nhi hua yaar")

### While loop conditions for counts with options###

x=2
while x<20:
    print(x)
    x=x+1
else:
    print("Ho gya count complete")


while x<25:
    print(x)
    x=x+1
    if x==23:
        print("%i yaane ki mere pe break aaya isiliye mein rukaya aur completed bola aur else ko ignore maara jo ki mere baad h" %x)
        break
else:
    print("Break ke wjh se ignore hota hoon mein")


## double the number and print till greater than 100 (useful for powers of 2 untill range given)
ic=1
while(ic < 100):
    print(ic)
    ic+=ic
    print(ic)