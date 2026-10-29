
#Parent Class/Super Class/Base Class
class Animal:

    isMammal = True
    age = 3

    def movement(self):
        print("Animal is moving")

#Child Class/Sub Class/Derived Class
class Dog(Animal):

    def bark(self):
        print("Woof! Woof!")

class Cat(Animal):

    def meow(self):
        print(" Meow! Meow!")

dog1 = Dog()
dog1.movement()
print(dog1.age,)

cat1 = Cat()
cat1.movement()
print(cat1.age)