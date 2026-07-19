while True:  
    print("""
====Notes App====
1. Add note
2. View notes
3. Exit""")

    command = input("Choice: ").strip().lower()

    if command == "1":
        note = input("Enter note: ").strip()
        if note:
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
            print("Note saved!")
        else:
            print("Note cannot be empty!")
    elif command == "2":
        try:
            with open("notes.txt", "r") as f:
                lines = f.readlines()
                if not lines:
                    print("note is empty")
                else:
                    for line in lines:
                        print(line.strip())
        except FileNotFoundError:
            print("""
There is no file created yet!
Press 1 to create and write notes.""")
    elif command == "3":
        print("Goodbye!")
        break
    else:
        print("""
Invalid choice!
Please choose 1, 2 or 3""")