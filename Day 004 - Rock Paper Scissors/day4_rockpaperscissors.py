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

import random
outcomes = [rock, paper, scissors]
choose = '''Please make a selection of what you would like to throw.
Type "rock", "paper", or "scissors"\n'''
choice = (input(choose)).lower()
if all([
    choice != "rock", 
    choice != "paper", 
    choice != "scissors",
    ]):
    print("You have made in invalid selection. Game over.")
else:
    if choice == "rock":
        chosen_outcome = rock
    elif choice == "paper":
        chosen_outcome = paper
    elif choice == "scissors":
        chosen_outcome = scissors
    random_outcome = outcomes[random.randint(0,len(outcomes)-1)]
    print(chosen_outcome)
    print(f"The computer chose {random_outcome}")
    if chosen_outcome == random_outcome:
        print("It is a draw.")
    elif chosen_outcome == rock and random_outcome == paper:
        print("You have lost.")
    elif chosen_outcome == paper and random_outcome == scissors:
        print("You have lost.")
    elif chosen_outcome == scissors and random_outcome == rock:
        print("You have lost.")
    else:
        print("You have won.")