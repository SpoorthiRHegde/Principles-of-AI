#program to find smallest number in a list
l1=[25,25,34,4,5]
min=l1[0]
for i in l1:
    if i<min:
        min=i
print("Smallest element",min)


#program to find largest number in a list
l1=[25,25,34,4,5]
max=l1[0]
for i in l1:
    if i>max:
        max=i
print("Largest element",max)



#program to find 2nd largest number in a list
l1=[25,25,34,4,5]
max=l1[0]
max2=0
for i in l1:
    if i>max:
        max2=max
        max=i
print("Second Largest element",max2)
