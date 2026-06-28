command = ""
print("Welcome to the Car Game")
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is started already!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is stopped already!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start
stop - to stop
quit - to quit""")
    elif command == "quit":
        print("Have a good one!")
        break
    else:
        print("""
Sorry, I don't understand this...
Type help for more info.""")
