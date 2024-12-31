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
player_hand = []
dealer_hand = []


def card():
    draw = random.choice(cards)
    return draw


def deal(hand: list):
    hand.append(card())
    return hand


def ace_check(hand: list):
    aces = 0
    for card in hand:
        if card == 11:
            aces += 1
    return aces


def hand_total(hand: list):
    total = 0
    total_B = 0
    score = {"score_A" : 0}
    total_aces = ace_check(hand)
    if total_aces == 0:
        for card in hand:
            total += card
        score["score_A"] = total
        return score
    elif total_aces == 1:
        for card in hand:
            if card != 11:
                total += card
                total_B += card
            else:
                total += card
                total_B += 1
        score["score_A"] = total
        score["score_B"] = total_B
        return score
    else:
        first_ace = 0
        for card in hand:
            if card == 11:
                first_ace += 1
                if first_ace == 1:
                    total += 11
                    total_B += 1
                else:
                    total += 1
                    total_B += 1
            else:
                total += card
                total_B += card
        score["score_A"] = total
        score["score_B"] = total_B
        return score
    

def display_total(hand: list):
    outcome = hand_total(hand)
    if len(outcome) == 1:
        score = outcome["score_A"]
        print(f"{player_hand} = {score}\nYou have {score}")
    else:
        score = outcome["score_A"]
        second_score = outcome["score_B"]
        if score > 21 and second_score < 21:
            print(f"{player_hand} = {second_score}\nYou have {second_score}")
        elif score == 21:
            print(f"You now have 21! Let's check to see if this beats the dealer's hand...")        
        else:
            print(f"{player_hand} = {second_score} / {score}\nYou have {second_score} or {score}")

        
def intial_deal():
    deal(player_hand)
    deal(dealer_hand)
    deal(player_hand)
    deal(dealer_hand)


def blackjack_check(hand):
    total = hand_total(hand)
    if total["score_A"] == 21:
        return "yes"
    else:
        return "no"
    

def blackjack_outcome(dealer, player):
    player_decision = True
    if blackjack_check(dealer) == "yes":
        if blackjack_check(player) == "yes":
            print(f"You have blackjack {player_hand} and the dealer has blackjack {dealer_hand}. This game ends in a tie.")
            player_decision = False
            return player_decision
        else:
            print(f"You have {player_hand} but the dealer has blackjack {dealer_hand}. This game immediately ends in a loss.")
            player_decision = False
            return player_decision
    elif blackjack_check(player) == "yes":
        print(f"You have blackjack! {player_hand} and the dealer has {dealer_hand}. You win immediately!")
        player_decision = False
        return player_decision
    else:
        return player_decision
    

def bust_check(hand: list):
    total = hand_total(hand)
    if len(total) == 1:
        if total["score_A"] > 21:
            bust_total = total["score_A"]
            print(f"You have busted with {bust_total}. This game ends in a loss.\nDealer had {dealer_hand}")
            return True
        else:
            return False
    else:
        if total["score_B"] > 21:
            bust_total = total["score_B"]
            print(f"You have busted with {bust_total}. This game ends in a loss.\nDealer had {dealer_hand}")
            return True
        else:
            return False
    

# def take_a_card(hand: list):
#     deal(hand)
#     busted = bust_check(hand)
#     if not busted:
#         another_choice = True
#     else:
#         another_choice = False
#     return another_choice


def player_turn(p_cards, d_cards):
    dealer_decision = True
    dealer_hole_card = dealer_hand[0]
    player_continue = blackjack_outcome(dealer_hand, player_hand)
    while player_continue:
        display_total(player_hand)
        count = hand_total(player_hand)
        if len(count) == 1:
            if count["score_A"] < 21:
                print(f"The dealer is showing {dealer_hole_card}: [{dealer_hole_card}, ?]")
                hit = input("Would you like to draw another card? Type \"y\" for yes or type \"n\" for no: ").lower()
                if hit == "y":
                    # os.system('clear')
                    deal(player_hand)
                    bust = bust_check(player_hand)
                    if bust:
                        dealer_decision = False
                        player_continue = False
                else:
                    player_continue = False
            elif count["score_A"] == 21:
                print(f"{player_hand} You have 21! Let's check to see if this beats the dealer's hand...")
                player_continue = False
            else:
                player_continue = False
        else:
            if count["score_A"] > 21:
                count = count["score_B"]
                if count < 21:
                    print(f"The dealer is showing {dealer_hole_card}: [{dealer_hole_card}, ?]")
                    hit = input("Would you like to draw another card? Type \"y\" for yes or type \"n\" for no: ").lower()
                    if hit == "y":
                        # os.system('clear')
                        deal(player_hand)
                        bust = bust_check(player_hand)
                        if not bust:
                            player_score = display_total(player_hand)
                            dealer_score = display_total(dealer_hand)
                            print(f"You have busted with {player_score}. This game ends in a loss.\nDealer had {dealer_score} {dealer_hand}")
                            dealer_decision = False
                            game_continue = False
                    else:
                        player_continue = False
                else:
                    print(f"{player_hand} You have 21! Let's check to see if this beats the dealer's hand...")
                    player_continue = False
            elif count["score_A"] == 21 or count["score_B"] == 21:
                print(f"{player_hand} You have 21! Let's check to see if this beats the dealer's hand...")
                player_continue = False
            else:
                print(f"The dealer is showing {dealer_hole_card}: [{dealer_hole_card}, ?]")
                hit = input("Would you like to draw another card? Type \"y\" for yes or type \"n\" for no: ").lower()
                if hit == "y":
                    # os.system('clear')
                    deal(player_hand)
                    bust = bust_check(player_hand)
                    if bust:
                        dealer_decision = False
                        player_continue = False
                else:
                    player_continue = False






intial_deal()
player_decision = blackjack_outcome(dealer_hand, player_hand)
if player_decision:
    # display_total(player_hand)
    player_turn(player_hand, dealer_hand)