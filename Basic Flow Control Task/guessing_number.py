def guessing_game():
    target_number = 58  # predefined number to guess
    attempts = 0
    is_guessed = False

    while not is_guessed:
        try:
            guess = int(input("Enter an integer between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess < 1 or guess > 100:
            print("Error: Number is not within the search range (1–100).")
            continue

        attempts += 1

        if guess < target_number:
            print("Too small")
        elif guess > target_number:
            print("Too large")
        else:
            print("Correct!")
            is_guessed = True

    print(f"Number of attempts: {attempts}")


guessing_game()
