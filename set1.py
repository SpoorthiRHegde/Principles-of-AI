#loop items
s1={1,2,3,4}
for x in s1:
    print(x)

#union
s2={5,6,7}
s3=s1.union(s2)
print(s3)

# | operator
s4=s1|s2
print(s4)

# join multiple sets
s5=s1.union(s2,s3)
print(s5)

s6=s1|s2|s3
print(s6)

#join list and tuple
t=(5,6,7)
s7=s1.union(t)
print(s7)

#update
s1.update(s2)
print(s1)

#insertion
s8=s1.intersection(s2)
print(s8)

s9=s1&s2
print(s9)

#differnce
s10={1,4,5,6}
s11=s1.difference(s10)
print(s11)

s12=s1-s10
print(s12)

#difference_update()
s1.difference_update(s10)
print(s1)

#symmetric_difference()
s13=s1.symmetric_difference(s10)
print(s3)

s14=s1^s10
print(s14)

#symmetric_difference_update()
s1.symmetric_difference_update(s10)
print(s1)

#discard()
s10.discard(1)
print(s10)

#isdisjoint()
a=s1.isdisjoint(s12)
print(a)

#issubset()
b=s1.issubset(s10)
print(b)

#issuperset()
c=s1.issuperset(s10)
print(c)
