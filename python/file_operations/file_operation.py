with open("file1.txt", "w") as f:
    f.write("Hello world")


with open("file1.txt", "r") as f:
    r = f.read()
    print(r)


with open("file1.txt", "w") as f:
    f.write("Python is fun")


with open("file1.txt", "r") as f:
    r = f.read()
    print(r)


with open("file1.txt", "a") as f:
    f.write("\nAppended line")


with open("file1.txt", "r") as f:
    r = f.read()
    print(r)


with open("file1.txt", "a") as f:
    f.write("\nAnother line\nLast line")

with open("file1.txt", "r") as f:
    r = f.read()
    print(r)
import os
os.remove("file1.txt")