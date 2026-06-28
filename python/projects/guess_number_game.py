secret_number = 6
guess_count = 1
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You lost!")