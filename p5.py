#Check if element exists in list in Python
def find(a,n):
    for i in a:
        if(i==n):
            return True
    return False
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
b=int(input("Enter the element to be searched:"))
print(find(a,b))


            
#pop() method to clear a list
l1=[1,2,3,4,5]
while(len(l1)!=0):
    l1.pop()
print("after deleting"+str(l1))



#reverse list
n=int(input("Enter the number of elements: "))
print("Enter the elements:")
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
def rever(a):
    n1=a[::-1]
    return n1
print("after reversing"+str(rever(a)))
