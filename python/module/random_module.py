import random

for i in range(3):
    print(random.random())


for i in range(3):
    print(random.randint(10, 20))

members = ["Max", "Lex", "Gagi", "Bob"]
leader = random.choice(members)
print(leader)