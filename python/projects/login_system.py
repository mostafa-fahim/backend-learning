while True:
    print("""
----Log in Page----
1. Register
2. Login
3. Exit""")
    
    try:
        choice = int(input("Choose 1/2/3: "))

        if choice not in (1, 2, 3):
            print("Please choose the right input")
            continue
        if choice == 3:
            print("good day ahead.")
            break
        
        user_name = input("User name: ")
        password = input("Password: ")

        if choice == 1:
            with open("user_log.txt", "a") as f:
                info = {
                    "user_name": user_name,
                    "password": password
                }
                f.write(str(info) + "\n")
                print("registered!")
        
        elif choice == 2:
            try:
                with open("user_log.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        if user_name and password not in line:
                            print("register first!")
                            continue
                    else:
                        print("logged in successfully")
            except FileNotFoundError:
                print("register first please")
    except ValueError:
        print("Please choose a valid input!")
