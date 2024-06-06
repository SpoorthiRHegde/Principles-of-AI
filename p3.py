#find the sum of array
a=[1,2,3]
sum=0
for i in a:
    sum=sum+i
print(sum)

# Find Largest Element in an Array
b=[2,3,4,3,1,4,5,2,5]
c=b[0]
for i in b:
    if c<i:
        c=i
print(c)

#rotation of array
def rotate(a,d):
    n=len(a)
    d=d%n
    return a[d:]+a[:d]
a=[1,2,4,5,7,8,9,5,6]
d=2
print(rotate(a,d))


#split an array and add it at end
def rev(a,k):
    return a[k:]+a[:k]
a=[1,2,3,4,5,6]
k=2
print(rev(a,k))
    
# Program for Find remainder of array multiplication divided by n
def pro(a,n):
    pro=1
    for i in a:
        pro=pro*i
    return pro%n
a=[100,10,5,25,35,14]
n=11
print(pro(a,n))

#check whether array is monotonic
def mono(x):
    y=x[:]
    z=x[:]
    y.sort()
    z.sort(reverse=True)
    if(x==y or x==z):
        return True
    return False
x=[2,4,2,4,5,7,1,0]
print(mono(x))
