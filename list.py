#craete list
l1=["a","b","c"]
print(l1)

#duplicate
l2=["a","b","c","a","b"]
print(l2)

#length
print(len(l2))

#diff datatype
l3=["a",2,"abc",2.5]
print(l3)

#type()
print(type(l3))

#list() constructor
l4=list(("a","b","c"))
print(l4)

#access items
print(l4[2])

#negative indexing
print(l4[-1])

#range of index
print(l2[2:5])
print(l2[:5])
print(l2[2:])
print(l2[-4:-1])

#check if the item exist
if "a" in l4:
    print("exists")

#change item vlaue
l2[2]="d"
print("l2")

#change a range of values
l2[1:3]=["a","b"]
print(l2)

#insert items
l1.insert(2,"c")
print(l1)

#append
l2.append("m")
print(l2)

#extend
l1.extend(l2)
print(l1)

#Add Any Iterable
t1=("n","l")
l3.extend(t1)
print(l3)

#remove
l1.remove("a")
print(l1)

#pop()
l1.pop(2)
print(l1)

l1.pop()
print(l1)

#del()
del l3

#clear()
l1.clear()
print(l1)


