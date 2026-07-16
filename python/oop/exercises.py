class Point:
    def move(self):
        print("move")


    def draw(self):
        print("draw")


point = Point()
point.draw()
point.move()


class Point:
    def move(self):
        print("move")


    def draw(self):
        print("draw")


point1 = Point()
point2 = Point()


point1.move()
point2.draw()

class Point:
    pass


point = Point()
point2 = Point()


point.x = 10
point.y = 12

point2.x = 22


print(point.x)
print(point2.x)
print(point.y)


class Dog:
    pass

dog1 = Dog()
dog2 = Dog()
dog3 = Dog()


print(type(dog1))


class Car:
    def start(self):
        print("start")


car1 = Car()
car1.start()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Fifi", 24)
person2 = Person("Gigi", 22)


print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


student1 = Student("Alex", 20)
student2 = Student("Max", 21)

print(student1.name, student1.roll)
print(student2.name, student2.roll)


class info:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = info(2, 5)
point2 = info(3, 6)

print(point1.x, point1.y)
print(point2.x, point2.y)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def talk(self):
        print(f"Hi my name is {self.name} and my age is {self.age}")


person1 = Person("Gigi", 22)

print(person1.name)
person1.talk()


class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        

car1 = Car("BMW", "M8")
print(car1.brand)
print(car1.name)


class Student:
    def __init__(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age


student1 = Student("Gagi", 12, 22)
print(f"Hello, my name is {student1.name}, my roll is {student1.roll} and my age is {student1.age}")


class Mammal:
    def walk(self):
        print("I am walking")


class Dog(Mammal):
    def bark(self):
        print("I just bark")


class Cat(Mammal):
    def meow(self):
        print("I just meow")


dog1 = Dog()
cat1 = Cat()
dog1.bark()
cat1.meow()


class Mammal:
    def walk(self):
        print("I am walking G")


class Cat(Mammal):
    def meow(self):
        print("meow")


cat1 = Cat()
cat1.meow()


class Vehicle:
    def start(self):
        print("started")

    
class Car(Vehicle):
    def color(self):
        print("black")


class Bike(Vehicle):
    def color(self):
        print("red")


car1 = Car()
bike1 = Bike()
car1.start()
car1.color()
bike1.start()
bike1.color()


class Animal:
    def eat(self):
        print("eating")


class Bird(Animal):
    def fly(self):
        print("I fly and fly")


bird = Bird()
bird.eat()
bird.fly()


class Mammal:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    
    def walk(self):
        print("I am just walking dude")


class Dog(Mammal):
    def bark(self):
        print("I like to bark yo")


dog = Dog("Maxo", 2)
dog.walk()
dog.bark()
print(f"My name is {dog.name}, and my age is {dog.age} and I like to bark")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def call(self):
        print(self.name, self.age)


person = Person("Laxo", 22)
print(person.name)
person.call()

class Phone:
    def __init__(self, brand):
        self.brand = brand

    
    def call(self):
        print(f"calling from the {self.brand} phone")


phone = Phone("Apple")
print(phone.brand)
phone.call()