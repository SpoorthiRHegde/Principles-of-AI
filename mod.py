#use a module
import mymodule
mymodule.greeting("john")

#variable in module
a=mymodule.p1["age"]
print(a)

#rename a module
import mymodule as mm
a=mm.p1["age"]
print(a)

#built in modules
import platform
x=platform.system()
print(x)

#dir()
y=dir(platform)
print(y)

from mymodule import p1
print(p1["age"])


