#for loop
a=["a","b","c"]
for x in a:
    print(x)

#loop through a string
for a in "hello":
    print(a)

#break
a=[1,2,3,4,5]
for x in a:
    print(x)
    if(x==3):
        break

#continue
a=[1,2,3,4,5]
for x in a:
    if(x==3):
        continue
    print(x)

#range function
for x in range(5):
    print(x)

for x in range(2,5):
    print(x)

for x in range(2,10,3):
    print(x)

#else in for loop
for x in range(6):
    print(x)
else:
    print("end of loop")

#nested loop
a=[1,2,3]
b=["a","b","c"]
for x in a :
    for y in b:
        print(x,y)

#pass statement
for x in [1,2,3]:
    pass
