class Mammal:
    def walk(self):
        print("I am walking my man")


class Dog(Mammal):
    def bark(self):
        print("I only bark bark and scare people")


class Cat(Mammal):
    def meow(self):
        print("I meow meow and steal food")


dog1 = Dog()
cat1 = Cat()
dog1.bark()
cat1.meow()