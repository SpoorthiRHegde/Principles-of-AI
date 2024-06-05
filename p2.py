#fibonacci
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
fib_series=[fib(i) for i in range(10)]
print(fib_series)

#palindrome
def palin(s):
    return s==s[::-1]
print(palin("radar"))

#prime number
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(prime(17))

#reverse a string
def rev(s):
    return s[::-1]
print(rev("hello"))

#area of the circle
def area(r):
    return 3.14*r*r
print(area(5))

#compound interest
def ci(p,r,t):
    a=p*(pow((1+r/100),t))
    i=a-p
    print("Compound interest",i)

ci(10000,10.25,5)

#armstrong number
def arm(n):
    a=n
    b=n
    sum=0
    i=0
    while n>0:
        n=n//10
        i=i+1
    while a>0:
        sum=sum+pow(a%10,i)
        a=a//10
    if(b==sum):
        print("yes")
    else:
        print("no")
arm(154)
