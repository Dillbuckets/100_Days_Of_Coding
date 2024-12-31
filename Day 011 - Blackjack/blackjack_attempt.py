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
dealer_hand_total = 0
alt_dealer_hand_total = 0
game_continue = True
dealer_turn = False
player_aces = 0
dealer_aces = 0
player_outcome = 0

def card():
    random_number = random.randint(0,12)
    draw = cards[random_number]
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
    score = []
    total_aces = ace_check(hand)
    if total_aces == 0:
        for card in hand:
            total += card
        score.append(total)
        return score
    elif total_aces == 1:
        for card in hand:
            if card != 11:
                total += card
                total_B += card
            else:
                total += card
                total_B += 1
        score.append(total)
        score.append(total_B)
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
        score.append(total)
        score.append(total_B)
        return score
    

    
def display_total(hand: list):
    outcome = []
    outcome = hand_total(hand)
    if len(outcome) == 1:
        outcome = outcome[0]
        return outcome
    else:
        if outcome[0] > 21:
            outcome = outcome[1]
        else:
            outcome = outcome[1], outcome[0]
            return outcome

        
def intial_deal():
    deal(player_hand)
    deal(dealer_hand)
    deal(player_hand)
    deal(dealer_hand)

intial_deal()
print(player_hand)
print(hand_total(player_hand))
print(dealer_hand)
print(hand_total(dealer_hand))
print((display_total(player_hand)))











def player_hand_total(hand, total, total_with_aces):
    if total == 21:
        print(f"{hand} You have 21! Let's check to see if this beats the dealer's hand...")
    elif total == total_with_aces:
        print(f"{hand} = {total} You have {total}")
    else:
        if total < 21:
            print(f"{hand} = {total_with_aces}/{total} You have {total_with_aces} or {total}")
        else:
            if total_with_aces < 21:
                print(f"{player_hand} You have 21! Let's check to see if this beats the dealer's hand...")
            else:
                print(f"{hand} = {total_with_aces} You have {total_with_aces}") 



            
    




    



        






# def dealer():
#     deal = True
#     player_aces = 0
#     dealer_aces = 0
#     global dealer_hand_total
#     global alt_dealer_hand_total
#     global game_continue
#     global player_outcome
#     while deal:
#         random_number = random.randint(0,12)
#         draw = cards[random_number]
#         if draw == 11:
#             player_aces += 1
#             if player_aces > 1:
#                 player_hand_total += 1
#                 alt_player_hand_total += 1
#             else:
#                 player_hand_total += 11
#                 alt_player_hand_total += 1
#         else:
#             player_hand_total += int(draw)
#             alt_player_hand_total += int(draw)
#         player_hand.append(draw)
#         if len(dealer_hand) < 2:
#             random_number = random.randint(0,12)
#             draw = cards[random_number]
#             if draw == 11:
#                 dealer_aces += 1
#                 if dealer_aces > 1:
#                     dealer_hand_total += 1
#                     alt_dealer_hand_total += 1
#                 else:
#                     dealer_hand_total += 11
#                     alt_dealer_hand_total += 1
#             else:
#                 dealer_hand_total += int(draw)
#                 alt_dealer_hand_total += int(draw)
#             dealer_hand.append(draw)
#         if len(player_hand) >= 2:
#             deal = False
#     if dealer_hand == [11, 10] or dealer_hand == [10, 11]:
#         if player_hand == [11, 10] or player_hand == [10, 11]:
#             print(f"You have blackjack {player_hand} and the dealer has blackjack {dealer_hand}. This game ends in a tie.")
#             game_continue = False
#             return
#         else:
#             print(f"You have {player_hand}\nThe dealer has blackjack {dealer_hand}. This game immediately ends in a loss.")
#             game_continue = False
#             return
#     if player_hand == [11, 10] or player_hand == [10, 11]:
#         print(f"You have blackjack! {player_hand}\nDealer has {dealer_hand}. You win immediately!")
#         game_continue = False
    if player_hand_total == 21 or alt_player_hand_total == 21:
        player_outcome = 21
        print(f"{player_hand} You have 21! Let's check to see if this beats the dealer's hand...")
        deal = False
    elif player_hand_total != alt_player_hand_total:
        if player_hand_total > 21:
            player_outcome = alt_player_hand_total
            print(f"You have {alt_player_hand_total}: {player_hand}")
        else:
            player_outcome = player_hand_total
            print(f"You have {alt_player_hand_total} or {player_hand_total}: {player_hand}")
    else:
        player_outcome = player_hand_total
        print(f"You have {player_hand_total}: {player_hand}")


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


def dealer_decision():
    global dealer_hand
    global dealer_hand_total
    global alt_dealer_hand_total
    global dealer_aces
    global player_outcome
    global game_continue
    dealer_turn = True
    dealer_outcome = 0
    print(dealer_aces)
    while dealer_turn:
        if dealer_hand_total >= 17 or alt_dealer_hand_total >= 17:
            dealer_turn = False
            game_continue = False
        else:
            random_number = random.randint(0,12)
            draw = cards[random_number]
            print(dealer_aces)
            if draw == 11:
                dealer_aces += 1
                if dealer_aces > 1:
                    dealer_hand_total += 1
                    alt_dealer_hand_total += 1
                else:
                    dealer_hand_total += 11
                    alt_dealer_hand_total += 1
            else:
                dealer_hand_total += int(draw)
                alt_dealer_hand_total += int(draw)
            dealer_hand.append(draw)
            if dealer_hand_total >= 17 or alt_dealer_hand_total >= 17:
                dealer_turn = False
                game_continue = False
    if dealer_hand_total > 21 and alt_dealer_hand_total > 21:
        print(f"{dealer_hand} The dealer has busted with {alt_dealer_hand_total}. You have won!")
        return
    elif dealer_hand_total != alt_dealer_hand_total:
        if dealer_hand_total > 21:
            dealer_outcome = alt_player_hand_total
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


# replay = True
# while replay:
#     print(logo)    
#     dealer()
#     dealer_hole_card = dealer_hand[1]
#     while game_continue:
#         player_decision()
#         while game_continue:
#             dealer_decision()
#     another_game = input("Would you like to play again? Type \"y\" for yes or type anything else to quit playing: ").lower()
#     # os.system('clear')
#     if another_game != "y":
#         replay = False
#     else:
#         player_hand = []
#         dealer_hand = []
#         player_hand_total = 0
#         alt_player_hand_total = 0
#         dealer_hand_total = 0
#         alt_dealer_hand_total = 0
#         game_continue = True
#         dealer_draw = False
#         player_aces = 0
#         dealer_aces = 0
#         player_outcome = 0

