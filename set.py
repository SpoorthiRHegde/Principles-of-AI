#set
s1={1,2,3,4}
print(s1)

#duplicate sets
s2={1,2,3,2,1}
print(s2)

s3={False,0,1}
print(s3)

#length
print(len(s3))

#type()
print(type(s3))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

#access item
for x in s1:
    print(x)

#check if item is present
print("banana" in thisset)

#check if item is not present
print("banana" not in thisset)

#add item
s1.add(5)
print(s1)

#add set
s2.update(s1)
print(s2)

#Add Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove item
s1.remove(2)
print(s1)

#discard item
s1.discard(1)
print(s1)

#pop
s1.pop()
print(s1)

#clear
s1.clear()
print(s1)

#delete
del s1
