# This is a Guessing game made By Sami as a one of CS50p project

import random


def main():
    # prompt user for a number between 1 and 10
    number = random.randint(1, 10)
    print("Welcome to the guessing game!")
    attempt = 0
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempt += 1  # Increment attempt count on each guess
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 10")
            elif guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print(
                    f"Congratulations! You guessed the number {number} in {attempt} attempts.")
                break  # Exit the loop when the correct number is guessed
        except ValueError:
            print("Invalid input. Please enter a valid number from 1 to 10.")


def Another_Game():
    while True:
        another_game = input(
            "Do you want to play again? (yes/no): ").strip().lower()
        if another_game == "yes":
            main()  # Restart the game if user chooses 'yes'
        elif another_game == "no":
            # Exit the game if user chooses 'no'
            print("Thank you for playing!")
            break
        else:
            # Handle invalid input
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()  # Start the game when the script is run
    Another_Game()  # Ask if the user wants to play again
