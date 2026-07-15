class Student:
    roll = ""
    gpa = ""


rahim = Student()
rahim.roll = 22
rahim.gpa = 2.2
print(f"Roll:{rahim.roll},GPA:{rahim.gpa}")


class Customer:
    name = ""
    city = ""
    number = ""


a = Customer()
a.name = "Lex"
a.city = "Dhaka"
a.number = 1111
b = Customer()
b.name = "Pex"
b.city = "Dhaka"
b.number = 2222
print(a.name, b.number)

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point2 = Point()
point2.move()
point2.y = 30
print(point1.x, point2.y)

class Teacher:
    group = ""
    subject = ""

max = Teacher()
max.group = "Science"
max.subject = "Biology"
alex = Teacher()
alex.group = "Science"
alex.subject = "Chemistry"
roger = Teacher()
roger.group = "Science"
roger.subject = "Physics"

point2.x = 22

print(max.subject, alex.group, roger.subject)