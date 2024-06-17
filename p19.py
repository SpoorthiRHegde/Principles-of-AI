#matrix creation
n=4
print("The dimension of the matrix",str(n))
x=n*n
y=[]
for i in range(1,x+1):
    y.append(i)
res=[]
i=0
while(i<len(y)):
    a=y[i:i+n]
    res.append(a)
    i=i+n
print("The craeted matrix of n*n:"+str(res))
