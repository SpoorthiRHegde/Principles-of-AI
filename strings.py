#display strings
print("hello")

#string ag array
a="hello"
print(a[2])

#looping through string
for x in "banana":
    print(x)

#length of string
print(len(a))

#check string
print("o" in a)

#check if not
print("w" not in a)

#slicing
b="Hello world"
print(b[2:5])

#slicing from start
print(b[:5])

#slicing in end
print(b[2:])

#slicing using negative indexing
print(b[-5:-2])

#upper case
print(b.upper())

#lower case
print(b.lower())

#remove whitespace
print(a.strip())

#replace string
print(b.replace("H","J"))

#split string
print(b.split(","))

#concatenate
x="hello"
y="world"
print(x+" "+y)

#fstring
a=25
t=f"my age is {a}"
print(t)

#escape characters
t="she said \"hello\" "
print(t)

#reverse string
print(x[::-1])
print("".join(reversed(x)))

#delete by slicing
print(y[:2]+y[3:])
