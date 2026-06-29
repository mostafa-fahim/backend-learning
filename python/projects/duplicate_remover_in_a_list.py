numbers = [2, 2, 4, 6, 8, 3, 5, 4, 5]
new = []
for number in numbers:
    if number not in new:
        new.append(number)
print(new)