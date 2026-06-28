name = input("Put your name here: ")
birth_year = int(input("Put your birth-year here: "))
age = 2026 - birth_year
if age >= 18:
    print(f"{name} is a {age} years old adult")
else:
    print(f"{name} is a {age} years old minor")
