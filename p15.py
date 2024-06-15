# Python program to print positive Numbers in a List
l1=[1,-5,9,-9,5,-7,-6]
num=0
while(num<len(l1)):
    if l1[num]<0:
        print(l1[num],end=" ")
    num=num+1
        
