#program to interchange first and last elements in a list
l1=[1,2,3,4,5]
def swap(a):
    a1=a[0]
    a[0]=a[len(a)-1]
    a[len(a)-1]=a1
    return a
print(swap(l1))

#Program to Swap Two Elements in a List
def swap1(a,i,j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    return a
l2=[1,2,3,4,5]
i=1
j=3
print(swap1(l2,i,j))

#Find the Length of a List in Python
l3=[1,2,3,4,5]
def length(a):
    i=0
    for j in a:
        i=i+1
    return i
print("Length of the list",length(l3))

# Find elements of a list by indices
lt1 = [10, 20, 30, 40, 50]
lt2 = [0, 2, 4]
def ind(a,b):
    c=[]
    for i in b:
        c.append(a[i])
    return c
print(ind(lt1,lt2))
