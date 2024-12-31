import random
from higher_lower_art import logo, vs
from higher_lower_game_data import data


def data_selector():
    selection = random.choice(data)
    return selection


def data_printer_compare(selected_entry_a):
    return print(f"Compare A: " + selected_entry_a['name'],", a", selected_entry_a['description'],", from", selected_entry_a['country'])


def data_printer_against(selected_entry_b):
    return print(f"Against B: " + selected_entry_b['name'],", a", selected_entry_b['description'],", from", selected_entry_b['country'])


def player_guess():
    guess = input("Who has more followers? Type \"A\" or \"B\":  ").lower()
    return guess


def correct_answer(sel_A, sel_B):
    followers_A = sel_A['follower_count']
    followers_B = sel_B['follower_count']
    if followers_A > followers_B:
        return "a"
    else:
        return "b"
    

def gameover(user_guess, comparison_answer):
    if user_guess == comparison_answer:
        return True
    else:
        return False
    

selection_A = {}
selection_B = {}
selection_B = data_selector()
score = 0
game_continues = True
print(logo)
while game_continues:
    selection_A = selection_B
    selection_B = data_selector()
    while selection_A == selection_B:
        selection_B = data_selector()
    data_printer_compare(selection_A)
    print(vs)
    data_printer_against(selection_B)
    right_answer = correct_answer(selection_A, selection_B)
    player_response = player_guess()
    print("\n" * 20)
    print(logo)
    game_continues = gameover(player_response, right_answer)
    if game_continues:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continues = False