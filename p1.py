#maximum of 2 numbers
def maximum(a, b):     
    if a >= b:
        return a
    else:
        return b
a = 2
b = 4
print(maximum(a, b))

#factorial number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
num = 5
print("Factorial of",num,"is",factorial(num))

#simple interest
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
    si = (p * t * r)/100
    print('The Simple Interest is', si)
    return si
simple_interest(8, 6, 8)
