#loop
d1={"name":"abc","age":34,"country":"india"}
for x in d1:
    print(x)

for x in d1:
    print(d1[x])

for x,y in d1.items():
    print(x,y)

#copy()
d2=d1.copy()
print(d2)

#dict()
d3=dict(d1)
print(d3)

#nested dict
d4={"s1":{
    "name":"aaa",
    "year":2004
    },
    "s2":{
        "name":"bbb",
        "year":2584
        },
    "s3":{
        "name":"ccc",
        "year":2587
        }}
print(d4)

c1={
    "name":"aaa",
    "year":2004
    }
c2={
        "name":"bbb",
        "year":2584
        }
c3={
        "name":"ccc",
        "year":2587
        }
c={"child1":c1,"child2":c2,"child3":c3}
print(c)

#access items
print(c["child2"]["name"])

#loop
for x, obj in c.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#setdefault():
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
