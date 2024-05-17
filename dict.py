#dictinaries
d1={"name":"aaa","year":2004}
print(d1)

#items
print(d1["year"])

#duplicate
thisdict = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2020}
print(thisdict)

#length
print(len(d1))

#type()
print(type(d1))

#dict() constructor
d2=dict(name="aaa",age=25,country="india")
print(d2)

#get()
print(d2.get("name"))

#add item
d2["dob"]="oct"
x=d2.keys()
print(x)

#values()
y=d2.values()
print(y)

#change
d2["name"]="abc"
print(d2)

#items()
z=d2.items()
print(z)

#check if key exists
if "name" in d2:
    print("Yes")

#update()
d2.update({"age":45})
print(d2)

#pop()
d2.pop("dob")
print(d2)

#popitems()
d1.popitem()
print(d1)

#del()
del d1["name"]
print(d1)

#clear()
d2.clear()
print(d2)

