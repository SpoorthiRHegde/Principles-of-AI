#parse json
import json
x='{"name":"John","age":38,"city":"india"}'
y=json.loads(x)
print(y["age"])

#json.dumps()
a={"name":"John","age":38,"city":"india"}
z=json.dumps(a)
print(z)

print(json.dumps({"name":"john","age":89}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps("hello"))
print(json.dumps(45))
print(json.dumps(25.68))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

b={
  "name":"John",
  "age":30,
  "married":True,
  "divorced":False,
  "children":("Ann","Billy"),
  "pets":None,
  "cars":[
    {"model":"BMW 230","mpg":27.5},
    {"model":"Ford Edge","mpg":24.1}
  ]
}
print(json.dumps(b))

#indent()
print(json.dumps(b,indent=4))
print(json.dumps(b,indent=4,separators=(". ","=")))

print(json.dumps(b,indent=4,sort_keys=True))
