#iterator
t1=(1,2,3)
myt1=iter(t1)
print(next(myt1))
print(next(myt1))
print(next(myt1))

str="banana"
mystr=iter(str)
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))
print(next(mystr))

#looping through iterator
for x in t1:
    print(x)

for x in str:
    print(x)
    
#create a iterator
class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=num()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#stop iterator
class num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=10:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=num()
myiter=iter(myclass)
for x in myiter:
    print(x)
    
