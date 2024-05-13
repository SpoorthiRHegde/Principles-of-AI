#loop through the list
l1=["a","b","c"]
for x in l1:
    print(x)

#Loop Through the Index Numbers
for x in range(len(l1)):
    print(l1[x])

#Using a While Loop
i=0
while i<len(l1):
    print(l1[i])
    i+=1

#Looping Using List Comprehension
[print (x) for x in l1]
    
#list comprhension
l2=["apple","mango","chikoo","kiwi"]
l3=[x for x in l2 if "a" in x]
print(l3)

l4=[x for x in l2 if x!="apple"]
print(l4)

l5=[x for x in l2]
print(l5)

l6=[x for x in range(3)]
print(l6)

l8 = [x for x in range(8) if x < 6]
print(l8)

l9=[x.upper() for x in l2]
print(l9)

l10=['hello' for x in l2]
print(l10)

l11=[x if x!="mango" else "orange" for x in l2]
print(l11)

#sort
l2.sort()
print(l2)

#sort descending
l2.sort(reverse=True)
print(l2)

#customize sort
def fun(n):
    return abs(n-50)

l7=[1000,52,45,85,96,75,36]
l7.sort(key=fun)
print(l7)

#case sensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse
l11.reverse()
print(l11)

#copy
l12=l11.copy()
print(l12)

l13=list(l12)
print(l13)

#join
l14=l2+l5
print(l14)

for x in l4:
    l1.append(x)
print(l1)

l3.append(l6)
print(l3)


                
