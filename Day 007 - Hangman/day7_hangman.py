
import random
import os

from day7_hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from day7_hangman_art import logo, stages
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
display = list(display)
guesses = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    guesses += guess
    os.system('clear')

    if guess in display:
        print(f"{guess} already chosen. Choose a different letter")
    else:        
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter
    
        #Check if user is wrong.
        if guess not in chosen_word:
            print(f'Your guess "{guess}" is not in the word. You lose a life.')
            lives -= 1
            if lives == 0:
                end_of_game = True
                # print("You lose.")
    
        #Join all the elements in the list and turn it into a String.
        print(f"You have guessed: {guesses}")
        print(f"{' '.join(display)}")
    
        #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(stages[lives])
if lives == 0:
    print(f"You have lost. Word was {chosen_word}")