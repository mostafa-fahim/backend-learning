# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# point = Point(22, 23)
# print(point.x, point.y)
# point.x = 25
# print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Hi, my name is {self.name}")


person1 = Person("Max")
person2 = Person("Bob")
person1.info()
person2.info()