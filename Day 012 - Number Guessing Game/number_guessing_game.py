import random
from number_guessing_game_art import logo

def select_number():
    """Selects a number for the game"""
    number = random.randint(1, 100)
    # print(f"Psst... the number is {number}")
    return number


def difficulty():
    """Allows the user to select the game difficulty and returns the total number of guesses they will have"""
    valid_selection = False
    total_guesses = 0
    while not valid_selection:
        difficulty_level = input("Choose a difficulty. Type \"easy\" or \"hard\":  ").lower()
        if difficulty_level == "easy":
            valid_selection = True
            print("You have 10 attempts to guess the number")
            total_guesses = 10
            return total_guesses
        elif difficulty_level == "hard":
            valid_selection = True
            print("You have 5 attempts to guess the number")
            total_guesses = 5
            return total_guesses
        else:
            valid_selection = False
            print("Please make a valid selction")
    print(valid_selection)


def guess(number, total_guesses):
    """Allows the user to try to guess the selected number, returns the outcome and number of turns remaining"""
    while total_guesses > 0:
        player_guess = int(input("Make a guess:  "))
        if player_guess == number:
            total_guesses = -1
            return print(f"You got it! The answer was {number}")
        elif player_guess > number:
            total_guesses -= 1
            print(f"Too high.\nGuess again.\nYou have {total_guesses} attempts remaining to guess the number.")
        else:
            total_guesses -= 1
            print(f"Too low.\nGuess again.\nYou have {total_guesses} attempts remaining to guess the number.")
    if total_guesses == 0:
        return print(f"You've run out of guesses, you lose. The number was {number}.")
    


def play_number_guessing_game():
    play_game = True
    while play_game:
        print(logo)
        print("Welcome to the Number Guessing Game!\nI'm think of a number between 1 and 100.")
        guess(select_number(), difficulty())
        if input("Would you like to play again? Type \"y\" for yes or enter anything else to exit game:  ") != "y":
            play_game = False
        else:
            print("\n" * 20)

play_number_guessing_game()