command = ""
while True:  
    print("""
    ====Notes App====
    1. Add note
    2. View notes
    3. Exit""")

    command = input("Choice: ").strip().lower()

    if command == "1":
        note = input("Enter note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
    elif command == "2":
        try:
            with open("notes.txt", "r") as f:
                for line in f:
                    print(line.strip())
        except Exception as e:
            print("""
There is no file created yet!
Press 1 to create and write notes.""")
    elif command == "3":
        print("Goodbye!")
        break
    