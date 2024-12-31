############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand_total = 0
alt_player_hand_total = 0
dealer_hand_total = 0
alt_dealer_hand_total = 0
game_continue = True
dealer_turn = False
player_aces = 0
dealer_aces = 0
player_outcome = 0

def ace_check(hand: list, draw: int):
    if draw != 11:
        return draw
    if 11 in hand:
        return 1
    else: 
        return 11



def player_decision():
    player_turn = True
    global dealer_turn
    global game_continue
    while player_turn:
        if player_hand_total < 21 or alt_player_hand_total < 21:
            print(f"The dealer is showing {dealer_hole_card}: [?, {dealer_hole_card}]")
            hit = input("Would you like to draw another card? Type \"y\" for yes or type \"n\" for no: ").lower()
            if hit == "y":
                os.system('clear')
                dealer()
                if player_hand_total > 21 and alt_player_hand_total > 21:
                    print(f"You have busted with {alt_player_hand_total}. This game ends in a loss.\nDealer had {dealer_hand_total} {dealer_hand}")
                    player_turn = False
                    game_continue = False
            else:
                dealer_turn = True
                player_turn = False
        elif player_hand_total == 21 or alt_player_hand_total == 21:
            dealer_turn = True
            player_turn = False



        
            if dealer_outcome > player_outcome:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a loss.")
            elif dealer_outcome == player_outcome:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a tie.")
            else:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nYou have won.")
        else:
            dealer_outcome = dealer_hand_total
            if dealer_outcome > player_outcome:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a loss.")
            elif dealer_outcome == player_outcome:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a tie.")
            else:
                print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nYou have won.")
    else:
        dealer_outcome = dealer_hand_total
        if dealer_outcome > player_outcome:
            print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a loss.")
        elif dealer_outcome == player_outcome:
            print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nThis game ends in a tie.")
        else:
            print(f"The dealer has {dealer_outcome}: {dealer_hand}\nYou have {player_outcome}: {player_hand}\nYou have won.")


def add_card(hand: list) -> list:
    random_number = random.randint(0,12)
    draw = cards[random_number]
    if draw == 11:
        draw = ace_check(hand, draw)
    hand.append(draw)
    return hand

def bust_check(hand: list):
    if sum(hand) > 21:
        return "bust"
    elif sum(hand) == 21:
        return "maybe win"
    elif sum(hand) >= 17:
        return "dealer holds"
    else:
        return "nothing special"



def main():
    replay = True
    while replay:
        player_hand = []
        dealer_hand = []
        print(logo)  
        player_hand = add_card(player_hand)
        dealer_hand = add_card(dealer_hand)
        player_hand = add_card(player_hand)
        dealer_hand = add_card(dealer_hand)
        player_bust_result = bust_check(player_hand)  
        dealer_bust_result = bust_check(dealer_hand)
        player_still_in = True
        dealer_still_in = True
        while player_still_in:
            hit = input("Would you like to draw another card? Type \"y\" for yes or type \"n\" for no: ").lower()
            if hit == "y":
                os.system('clear')
                add_card(player_hand)
                bust_result = bust_check(player_hand)
                print(f"You have busted with {alt_player_hand_total}. This game ends in a loss.\nDealer had {dealer_hand_total} {dealer_hand}")
        another_game = input("Would you like to play again? Type \"y\" for yes or type anything else to quit playing: ").lower()
        # os.system('clear')
        if another_game != "y":
            replay = False
            player_hand_total = 0
            alt_player_hand_total = 0
            dealer_hand_total = 0
            alt_dealer_hand_total = 0
            game_continue = True
            dealer_draw = False
            player_aces = 0
            dealer_aces = 0
            player_outcome = 0

if __name__== "__main__":
    main()