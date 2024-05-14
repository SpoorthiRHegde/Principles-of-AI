#tuple
t1=("a","b","c","j")
print(t1)

#length
print(len(t1))

#create a tuple with one item
t2=("a",)
print(type(t2))

#tuple constructor
t3=tuple(("a","b","c","d","e","f"))
print(t3)

#access tuple item
print(t3[2])

print(t3[-1])

print(t3[2:5])

print(t3[:4])

print(t3[3:])

print(t3[:4])

print(t3[-7:-4])

#check if item exist
if "d" in t3:
    print("yes")

#chaging tuple values
x=list(t1)
x[1]="k"
t1=tuple(x)
print(x)

#add items
x=list(t1)
x.append("g")
t1=tuple(x)
print(t1)

#add tuple to tuple
t2=t2+t1
print(t2)

#removing items
x=list(t1)
x.remove("a")
t1=tuple(x)
print(t1)

#delete a tuple
del t2

#unpacking a tuple
t4=("a","b","c")
(A,B,C)=t4
print(A)
print(B)
print(C)

#using *
(A,B,*C)=t1
print(A)
print(B)
print(C)

(A,*B,C)=t1
print(A)
print(B)
print(C)

#loop through tuple
for x in t1:
    print(x)

#loop using index
for x in range(len(t1)):
    print(t1[x])

#loop using while:
i=0
while i<len(t1):
    print(t1[i])
    i=i+1

#join tuple
t5=t3+t4
print(t5)

#multiply tuple
t6=t5*2
print(t6)

#count
a=t6.count("b")
print(a)








