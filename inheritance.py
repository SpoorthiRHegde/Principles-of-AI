#parent class
class person:
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
    def print(self):
        print(self.f,self.l)
x=person("aaa","bbb")
x.print()

#child class
class student(person):
    pass

y=student("ccc","ddd")
y.print()

class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)

#super()
class student(person):
    def __init__(self,fname,lname):
        super().__init__(self,fname,lname)

#add properties
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.grad=2015
z=student("eee","fff",2019)

#add methods
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.grad=year
    def welcome(self):
        print("welcome",self.f,self.l,"to the class of ",self.grad)
a=student("bbb","vvv",2015)
a.welcome()
