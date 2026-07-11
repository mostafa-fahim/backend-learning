def greet_user(name):
    print(f"Hi {name}")
    print("Welcome to the team")


greet_user("Lali")

def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome to the team man")


print("Start")
greet_user("John", "Max")
greet_user(first_name="Rick", last_name= "Mama")
greet_user("Nano", last_name= "John")
print("Finish")