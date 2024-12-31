import random
import os
from blackjack_art import logo
player_hand = []
dealer_hand =[]
game_ends = False
dealer_score = -1
player_score = -1
play_again = True


def deal_card():
    """Returns a card at random from the list of availalble cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(hand):
    """Take a list of card values and return their total added together"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(p_score, d_score):
    # if p_score == 0 and d_score == 0:
    #     return print(f"You {player_hand} and the dealer {dealer_hand} both have blackjack. The game ends in a draw.")
    # elif p_score == d_score:
    #     return print(f"Both you {player_hand} and the dealer {dealer_hand} have {player_score}. The game ends in a draw.")
    # elif p_score == 0:
    #     return print(f"BLACKJACK!!! You win the game immediately!")
    # elif d_score == 0:
    #     return print(f"You have {player_hand} and the dealer {dealer_hand} has blackjack. You have lost this game.")
    # elif p_score > 21:
    #     return print(f"You {player_hand} have busted with {player_score} and you have lost. Dealer had {dealer_hand}")
    # elif d_score > 21:
    #     return print(f"The dealer {dealer_hand} has busted with {dealer_score}! You have won this game!")
    # elif p_score > d_score:
    #     return print(f"You {player_hand} have {player_score} and the dealer {dealer_hand} has {dealer_score}. You have won this game!")
    # else:
    #     return print(f"You {player_hand} have {player_score} and the dealer {dealer_hand} has {dealer_score}. You have lost this game.")
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_blackjack():
    print(logo)
    player_hand = []
    dealer_hand =[]
    game_ends = False
    dealer_score = -1
    player_score = -1


    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())


    while not game_ends:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards: {player_hand}, current score {player_score}")
        print(f"Dealer is showing: {dealer_hand[0]} ")


        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_ends = True
        else:
            choice = input("Type \"y\" to draw another card or type \"n\" to keep your score: ").lower()
            if choice == "y":
                player_hand.append(deal_card())
            else:
                game_ends = True


    while dealer_score < 17 and dealer_score != 0:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))
    print("\n")


while input("Type \"y\" to play a game of blackjack or enter anything else to exit: ").lower() == "y":
    print("\n" * 20)
    play_blackjack()