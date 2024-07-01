# Class definition for a simple Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 5)
print(my_dog.bark())
