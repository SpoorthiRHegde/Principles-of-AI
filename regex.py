#regex
import re
t="Welcome for python"
x=re.search("^The,*for$",t)
if x:
    print("yes")
else:
    print("no")

#findall()
a=re.findall("me",t)
print(a)

#search()
b=re.search("\s",t)
print("The first white space character is at ",b.start())

#split()
c=re.split("\s",t)
print(c)

#sub()
d=re.sub("\s","9",t,2)
print(d)

#span()
e=re.search(r"\bW\w+",t)
print(e.span())

#string
f=re.search(r"\bW\w+",t)
print(f.string)

#group()
g= re.search(r"\bW\w+",t)
print(g.group())
