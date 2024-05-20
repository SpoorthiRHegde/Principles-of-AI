#class polymorphism:
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")
car1=car("aaa","bbb")
boat1=boat("ccc","ddd")
plane1=plane("eee","fff")
for x in (car1,boat1,plane1):
    x.move()

#class inheritance
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")
class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
car1=car("aaa","bbb")
boat1=boat("ccc","ddd")
plane1=plane("eee","fff")
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
