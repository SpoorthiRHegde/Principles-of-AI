#function
def a():
    print("hello")

a()

#arguements
def b(name):
    print("hello"+name)

b("sam")
b("jim")

#number of arguements
def c(n1,n2):
    print("hello "+n1+" and "+n2)

c("sam","jim")

#arbitrary arguements
def d(*name):
    print("hello"+name[2])
d("sam","jim","john")

#keyword arguements
def d(n1,n2,n3):
    print("hello"+n3)
d(n1="sam",n2="jim",n3="john")

#arbitrary keyword arguemnts
def e(**name):
    print("second person"+name["n2"])
e(n1="sam",n2="jim",n3="john")

#default parameter
def f(n="a"):
    print("Hello"+n)
f("sam")
f()
f("jim")

#Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#retruning values
def g(x):
    return x*x
print(g(5))
print(g(3))

#pass
def h():
    pass

#recursion
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
num = 6
if num < 0:
    print("Invalid input ! Please enter a positive number.")
elif num == 0:
    print("Factorial of number 0 is 1")
else:
    print("Factorial of number", num, "=", fact(num))
