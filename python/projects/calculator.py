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

        if choice == 1:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            result = first + second
            print(f"Result: {result}")
        
        elif choice == 2:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            result = first - second
            print(f"Result: {result}")
            
        elif choice == 3:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            result = first * second
            print(f"Result: {result}")

        elif choice == 4:
            try:
                first = float(input("First number: "))
                second = float(input("Second number: "))
                result = first / second
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Cannot divide by zero!")

        elif choice == 5:
            print("Have a good day!")
            break

        else:
            print("Invalid input!\nChoose a valid number.")
        
    except ValueError:
        print("Invalid input!\nChoose a valid number.")

    
    
