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