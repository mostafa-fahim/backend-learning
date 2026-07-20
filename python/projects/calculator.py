while True:
    print("""
    ====Calculator====
    1. Add
    2. subtract
    3. Multiply
    4. Divide      
    5. Exit
    """)

    try:
        choice = int(input("Choice: "))

        if choice == 5:
            print("Have a good day!")
            break

        if choice not in (1, 2, 3, 4):
            print("invalid choice, choose 1, 2, 3 or 4")
            continue

        first = float(input("First number: "))
        second = float(input("Second number: "))

        if choice == 1:
            result = first + second
            print(f"Result: {result}")
        
        elif choice == 2:
            result = first - second
            print(f"Result: {result}")
            
        elif choice == 3:
            result = first * second
            print(f"Result: {result}")

        elif choice == 4:
            try:
                result = first / second
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Cannot divide by zero!")

        else:
            print("Invalid input!\nChoose a valid number.")
        
    except ValueError:
        print("Invalid input!\nChoose a valid number.")

    
    
