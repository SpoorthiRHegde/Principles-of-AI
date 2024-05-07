#if elif else
a=200
b=333
if a>b:
    print("A i greater")
elif a<b:
    print("B is greater")
else:
    print("equal")

#and
c=450
if b>a and c>a:
    print("and condition")

#or
if b>a or c>a:
    print("or condition")

#not
if not a>b:
    print("a is not greater than b")

#nested if
x=15
if x>10:
    if x>20:
        print("Greater than 20")
    else :
        print("between 10 and 20")
else:
    print("less than 10")

#pass:empty if
if x>40:
    pass

#while loop
i=1
while i<5:
    print(i)
    i=i+1

#break
i=1
while i<5:
    print(i)
    if i==3:
        break
    i=i+1

#continue
i=1
while i<5:
    print(i)
    i=i+1
    if i==3:
        continue
    

 
#while else
i=1
while i<5:
    print(i)
    i=i+1
else:
    print("i is 5")
