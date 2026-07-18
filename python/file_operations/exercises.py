#exercise-1
with open("file2.txt", "w") as f:
    f.write("\nLine1\nLine2\nLine3")


with open("file2.txt", "r") as f:
    content = f.read()
    print(content)


content = content.replace("Line2", "Replaced line")


with open("file2_modified.txt", "w") as f:
    f.write(content)


with open("file2_modified.txt", "r") as f:
    print(f.read())


with open("file2_modified.txt", "r") as f:
    content = f.read()


content = content.replace("Line1", "First").replace("Line3", "Third")


with open("file2_final.txt", "w") as f:
    f.write(content)


with open("file2_final.txt", "r") as f:
    print(f.read())
