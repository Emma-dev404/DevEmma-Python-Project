#class - is a blueprint of an object
#Object - is an instance of a class

class Employee:      #creating a class


    def __init__(self, name, gender, position, age):  #init allows us to pass the values to specific objects as parameters
        self.name = name
        self.gender = gender
        self.position = position
        self.age = age

    def drive(self):         #the function
        print("Employee is driving")

    def eat(self):
        print("Employee is eating")


employee1 = Employee( "Reynold", "Male", "Managing Director", 32)  #Creating an object
print(employee1.name, employee1.gender, employee1.position, employee1.age)
employee1.drive()


employee2 = Employee( "Emma", "Female", "Admin", 28)
print(employee2.name, employee2.gender, employee2.position, employee2.age)
employee2.eat()


employee3 = Employee( "Juliana", "Female", "Secretary", 17)
print(employee3.name, employee3.gender, employee3.position, employee3.age)
employee3.drive()