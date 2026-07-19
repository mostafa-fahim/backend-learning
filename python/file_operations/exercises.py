# #exercise-1
# with open("file2.txt", "w") as f:
#     f.write("\nLine1\nLine2\nLine3")


# with open("file2.txt", "r") as f:
#     content = f.read()
#     print(content)


# content = content.replace("Line2", "Replaced line")


# with open("file2_modified.txt", "w") as f:
#     f.write(content)


# with open("file2_modified.txt", "r") as f:
#     print(f.read())


# with open("file2_modified.txt", "r") as f:
#     content = f.read()


# content = content.replace("Line1", "First").replace("Line3", "Third")


# with open("file2_final.txt", "w") as f:
#     f.write(content)


# with open("file2_final.txt", "r") as f:
#     print(f.read())


#exercie-2
with open("fruits.txt", "w") as f:
    f.write("apple\nbanan\norange")


count = 0
with open("fruits.txt", "r") as f:
    for line in f:
        count += 1
        print(line.strip())
    
print(f"Total line: {count}")