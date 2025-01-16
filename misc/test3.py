rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Put the available choice in a list
options = [rock, paper, scissors]

# Ask the user to make a selection of the three choices
player_selection = int(input("What do you choose? \"0\" for rock \"1\" for paper \"2\" for scissors:\n"))

# Show the player the choice they have made, referencing the image from the list we made with the user choice
print("Your choice")
print(options[player_selection])

# Have the computer make a choice

import random
computer_choice = random.randint(0, 2)

# Show the player the choice the computer has made, referencing the image from the list we made with the user choice
print("Their choice")
print(options[computer_choice])

# Determine the winner, comparing the choices with "if" statements
# Use player_choice vs computer_choice
# Print the winner

if player_selection > computer_choice:
    if player_selection == 2 and computer_choice == 0:
        print("You lose")
    else:
        print("You win")
elif player_selection == computer_choice:
    print("It's a draw")
else:
    if computer_choice == 2 and player_selection == 0:
        print("You win")
    else:
        print("You lose")