#create class
class cls:
    x=5

#create object
p1=cls()
print(p1.x)

#_init_()
class fruit:
    def __init__(self,name,price):
        self.n=name
        self.p=price
f1=fruit("apple",10)
print(f1.n)
print(f1.p)

#__str__() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

#object methods
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun(self):
        print("name: "+self.name)
        print("age: "+str(self.age))

p1=person("john",36)
p1.fun()

#self parameter
class per:
    def __init__(random,name,age):
        random.name=name
        random.age=age

    def func(random):
        print("name: "+random.name)
        print("age: "+str(random.age))

pr1=person("john",36)
pr1.fun()

#modify object properties:
p1.age=89
print(p1.age)

#delete object properties
del p1.age

#delete object
del p1

#pass statement
class abc:
    pass

