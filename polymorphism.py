#Polymorphism - many forms ; method has same name but different behaviour.

class Dog:
    def sound(self):
        print("The dog barks!")

class Cat:
    def sound(self):
        print("The cat meows!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#polymorphsm using loop (for loop)

class Dog:
    def sound(self):
        print("Bark!")

class Cat:
    def sound(self):
        print("Meow!")

class Cow:
    def sound(self):
        print("Moo!")

animal = (Dog(), Cat(), Cow())
for animal in animal:
    animal.sound()

#types of polymorphism[Duck typing, Override, operator]
#Duck typing
class Phone:
    def sound(self):
        print("Making a call")

class Computer:
    def sound(self):
        print("Running a program")

def operate(device):
    device.use()

operate(Computer())
operate(Phone())

#Override

class Animal:
    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Dog()
animal.sound()

#operator
