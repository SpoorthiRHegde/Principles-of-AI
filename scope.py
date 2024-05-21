#local scope
def fun():
    x=30
    print(x)
fun()

#function inside function
def fun1():
    x=10
    def fun2():
        print(x)
    fun2()
fun1()

#global scope
y=25
def fun3():
    print(y)
fun3()
print(y)

z=255
def fun4():
    z=25
    print(z)
fun4()
print(z)

#global keyword
def fun5():
    global a
    a=47
fun5()
print(a)

b=2555
def fun6():
    global b
    b=58
fun6()
print(b)

#non local keyword
def myfunc1():
  x = 9
  def myfunc2():
    nonlocal x
    x = 2004
  myfunc2()
  return x

print(myfunc1())
