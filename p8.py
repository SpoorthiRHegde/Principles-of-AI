n=int(input("Enter the number of elements: "))
print("Enter the elements:")
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
m,n=map(int,input("enter the range in which the values should lie").split())
print("even elements in the range ",m,n,"are")
for i in a:
    if i%2==0 and i>m and i<n:
        print(i," ")


n=int(input("Enter the number of elements: "))
print("Enter the elements:")
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
m,n=map(int,input("enter the range in which the values should lie").split())
print("odd elements in the range ",m,n,"are")
for i in a:
    if i%2!=0 and i>m and i<n:
        print(i," ")


