import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)

    # Maximum number of attempts
    max_attempts = 3
    attempts = 0

    # Start the game loop
    while attempts < max_attempts:
        try:
            # Get user's guess
            guess = int(input(" Enter your guess: "))

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                break
            else:
                print("Sorry, Try again.")

            # Increase the number of attempts
            attempts += 1

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # If max attempts reached and no correct guess
    if attempts == max_attempts and guess != secret_number:
        print(f"Game over! The correct number was {secret_number}.")

    # Ask to play again
    play_again = input("\n Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thanks for playing! Goodbye.")

# Run the game
number_guessing_game()
