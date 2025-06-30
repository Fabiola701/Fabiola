import random

# Function to generate a random number between 1 and 100
def generate_random_number():
    """
    Generates a random integer between 1 and 100 (inclusive).
    """
    return random.randint(1, 100)

# Function to get the user's guess and validate it
def get_user_guess():
    """
    Prompts the user to enter a guess and validates if it's an integer.
    Continuously prompts until valid input is received.
    """
    while True: # While loop to ensure valid integer input
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Your guess is out of range. Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Function to play a single round of the game
def play_game():
    """
    Contains the main logic for one round of the number guessing game.
    It generates a random number, handles user guesses, and checks for win/loss conditions.
    """
    secret_number = generate_random_number()
    attempts = 0
    max_attempts = 10
    has_won = False

    print("\nI'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    # For loop to limit the number of attempts
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt}/{max_attempts}")
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempts} attempts.")
            has_won = True
            break # Exit the for loop if the number is guessed

    if not has_won:
        print(f"\nGame over! You ran out of attempts.")
        print(f"The secret number was: {secret_number}")

    return has_won # Return whether the user won or lost

# Main function to control the game flow and "play again" loop
def main():
    """
    The main function that orchestrates the game.
    It includes a while loop to allow the user to play multiple rounds.
    """
    play_again = True
    while play_again: # While loop to keep playing until the user quits
        play_game() # Play one round of the game

        while True: # Inner while loop for valid play again input
            choice = input("Do you want to play again? (yes/no): ").lower().strip()
            if choice == "yes":
                play_again = True
                break # Exit inner loop, continue outer game loop
            elif choice == "no":
                play_again = False
                break # Exit inner loop, then outer game loop
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

    print("\nThanks for playing! Goodbye.")

# Entry point of the program
if __name__ == "__main__":
    main() # Call the main function to start the game
