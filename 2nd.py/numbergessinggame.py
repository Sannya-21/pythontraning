secret = 25
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret:
        print("Too High")
    elif guess < secret:
        print("Too Low")
    else:
        print("Correct Guess!")
        print("Attempts taken:", attempts)
        break