n=int(input("Enter the number of elements: "))
print("Enter the elements:")
a=[]
for i in range(n):
    ele=int(input())
    a.append(ele)
print("even elements are")
for i in a:
    if i%2==0:
        print(i," ")


n=int(input("Enter the number of elements: "))
print("Enter the elements:")
b=[]
for i in range(n):
    ele=int(input())
    b.append(ele)
print("odd elements are")
for i in b:
    if i%2!=0:
        print(i," ")
