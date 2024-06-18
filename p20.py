n=4
print("The dimension od the matrix:"+str(n))
res=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(1+n*i+j)
    res.append(row)
print("The crated matrix of n*n :"+str(res))
